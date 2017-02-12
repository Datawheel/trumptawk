# TrumpTawk
A quick hack that lets you make the Donald say what he means.

# Contribute!
Help expand what users can express! Use your favorite video editor and trim words spoken on video by Donald from publically available speeches.

Using ffmpeg we've been transcoding new video files (assuming we had a word.mov file) as follows:

```ffmpeg -an -i word.mov -movflags +faststart -vcodec libx264 -pix_fmt yuv420p -profile:v baseline -level 3 word.mp4```
