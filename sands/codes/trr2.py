ffmpeg -i aud1.mp3 -vn -acodec pcm_s16le -ac 1 -ar 44100 -f wav foo.wav
