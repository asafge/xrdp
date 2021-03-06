#ifndef OURINTERFACE_H
#define OURINTERFACE_H

#ifdef __cplusplus
#define __STDC_CONSTANT_MACROS
#ifdef _STDINT_H
#undef _STDINT_H
#endif
#include <stdint.h>
#endif

#include <QObject>
#include <QRect>
#include <QDebug> // LK_TODO

#include "xrdpvr.h"
#include "xrdpapi.h"
#include "demuxmedia.h"
#include "playvideo.h"

/* ffmpeg related stuff */
extern "C"
{
    #include <libavformat/avformat.h>
    #include <libavcodec/avcodec.h>
}

class OurInterface : public QObject
{
    Q_OBJECT

public:
    explicit OurInterface(QObject *parent = 0);
    
    /* public methods */
    int  oneTimeInit();
    void oneTimeDeinit();
    void initRemoteClient();
    void deInitRemoteClient();
    int  sendGeometry(QRect rect);
    void setFilename(QString filename);
    void playMedia();
    PlayVideo *getPlayVideoInstance();
    void setVcrOp(int op);

public slots:
    void onGeometryChanged(int x, int y, int width, int height);

signals:
    void on_ErrorMsg(QString title, QString msg);
    void onMediaDurationInSeconds(int duration);

private:

    /* private stuff */
    QQueue<MediaPacket *> audioQueue;
    QQueue<MediaPacket *> videoQueue;

    DemuxMedia     *demuxMedia;
    QThread        *demuxMediaThread;
    PlayVideo      *playVideo;
    QString         filename;
    void           *channel;
    int             stream_id;
    QRect           savedGeometry;

    /* private methods */
    int  openVirtualChannel();
    int  closeVirtualChannel();
    int  sendMetadataFile();
    int  sendVideoFormat();
    int  sendAudioFormat();
};

#endif // INTERFACE_H
