EXTRA_DIST = bootstrap COPYING design.txt faq-compile.txt faq-general.txt file-loc.txt install.txt prog_std.txt readme.txt

if XRDP_FREERDP1
FREERDPDIR = freerdp1
else
FREERDPDIR =
endif

if XRDP_NEUTRINORDP
NEUTRINORDPDIR = neutrinordp
else
NEUTRINORDPDIR =
endif
 
if XRDP_XRDPVR
XRDPVRDIR = xrdpvr
else
XRDPVRDIR =
endif

if SESMAN_DUALMON
DUALMONDIR = dualmon
else
DUALMONDIR =
endif

SUBDIRS = \
  common \
  vnc \
  rdp \
  xup \
  mc \
  $(FREERDPDIR) \
  $(NEUTRINORDPDIR) \
  libxrdp \
  xrdp \
  sesman \
  keygen \
  docs \
  instfiles \
  genkeymap \
  xrdpapi \
  $(XRDPVRDIR) \
  $(DUALMONDIR)
