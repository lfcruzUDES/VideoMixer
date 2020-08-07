for f in *.MTS; echo $f| awk 'BEGIN {FS = "."}{if($1 > 33){system("ffmpeg -i "$f" -strict -2  -deinterlace "$1".mp4")}}'

ffmpeg -f concat -safe 0 -i videos.txt -c copy video.MTS 

ffmpeg -i 00048.MTS -ss 00:00:00 -t 00:00:11 -async 1 00048_OK.MTS