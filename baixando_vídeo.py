from pytube import Youtube

video = Youtube("https://www.youtube.com/watch?v=EF889gHjZu8")

stream = video.stream.get_highest_resolution()

stream.download(output_path="./saida")