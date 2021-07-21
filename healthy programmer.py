 def musiconloop(file,stopper):
     mixer.init()
     mixer.music.load(file)
     mixer.music.play()
     while True:
         a= input()
         if a==stopper:
             mixer.music.stop()
             break