/**
 * xrdp: A Remote Desktop Protocol server.
 *
 * Copyright (C) Jay Sorg 2004-2012
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 *
 * @file session.h
 * @brief Session management definitions
 * @author Jay Sorg, Simone Fedele
 *
 */


#ifndef SESSION_H
#define SESSION_H

#include "libscp_types.h"

#define SESMAN_SESSION_TYPE_XRDP  1
#define SESMAN_SESSION_TYPE_XVNC  2

#define SESMAN_SESSION_STATUS_ACTIVE        0x01
#define SESMAN_SESSION_STATUS_IDLE          0x02
#define SESMAN_SESSION_STATUS_DISCONNECTED  0x04
/* future expansion
#define SESMAN_SESSION_STATUS_REMCONTROL    0x08
*/
#define SESMAN_SESSION_STATUS_ALL           0xFF

#define SESMAN_SESSION_KILL_OK        0
#define SESMAN_SESSION_KILL_NULLITEM  1
#define SESMAN_SESSION_KILL_NOTFOUND  2

struct session_date
{
  tui16 year;
  tui8  month;
  tui8  day;
  tui8  hour;
  tui8  minute;
};

#define zero_time(s) { (s)->year=0; (s)->month=0; (s)->day=0; (s)->hour=0; (s)->minute=0; }

struct session_item
{
  char name[256];
  int pid; /* pid of sesman waiting for wm to end */
  int display;
  int width;
  int height;
  int bpp;
  long data;

  /* status info */
  unsigned char status;
  unsigned char type;

  /* time data  */
  struct session_date connect_time;
  struct session_date disconnect_time;
  struct session_date idle_time;
  char client_ip[256];
};

struct session_chain
{
  struct session_chain* next;
  struct session_item* item;
};

/**
 *
 * @brief finds a session matching the supplied parameters
 * @return session data or 0
 *
 */
struct session_item* DEFAULT_CC
session_get_bydata(char* name, int width, int height, int bpp, int type);
#ifndef session_find_item
  #define session_find_item(a, b, c, d, e) session_get_bydata(a, b, c, d, e);
#endif

/**
 *
 * @brief starts a session
 * @return 0 on error, display number if success
 *
 */
int DEFAULT_CC
session_start(int width, int height, int bpp, char* username, char* password,
              long data, tui8 type, char* domain, char* program,
              char* directory, char* client_ip);

int DEFAULT_CC
session_reconnect(int display, char* username);

/**
 *
 * @brief starts a session
 * @return error
 *
 */
int APP_CC
session_sync_start(void);

/**
 *
 * @brief kills a session
 * @param pid the pid of the session to be killed
 * @return
 *
 */
int DEFAULT_CC
session_kill(int pid);

/**
 *
 * @brief sends sigkill to all sessions
 * @return
 *
 */
void DEFAULT_CC
session_sigkill_all();

/**
 *
 * @brief retrieves a session's descriptor
 * @param pid the session pid
 * @return a pointer to the session descriptor on success, NULL otherwise
 *
 */
struct session_item* DEFAULT_CC
session_get_bypid(int pid);

/**
 *
 * @brief retrieves a session's descriptor
 * @param pid the session pid
 * @return a pointer to the session descriptor on success, NULL otherwise
 *
 */
struct SCP_DISCONNECTED_SESSION*
session_get_byuser(char* user, int* cnt, unsigned char flags);

#endif
