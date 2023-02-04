import pygame as pg
pg.mixer.init()
pg.font.init()
pg.init()




class Game :
	def __init__ (self) :
		#### config
		self.size, self.title = (600, 900), 'JPBB composer | V 1.0'
		self.fps, self.timeMult = 60, 1

		#### window
		self.window = pg.display.set_mode(self.size)
		self.clock  = pg.time.Clock()

		#### gameplay
		self.state = 'song_menu'


	def update (self) :
		if self.mode == 'recording' :
			self.time += 5

			keys = pg.key.get_pressed()

			if keys[pg.K_LCTRL] :
				if keys[pg.K_s] : self.saveSong()
				if keys[pg.K_o] : self.openSong()

			if keys[pg.K_ESCAPE] : self.running = 0


	def render (self) :
		self.window.fill((0, 0, 0))
		#### render

		pg.draw.line(self.window, (255, 255, 255), (62, 800), (562, 800), 3)

		for x in range(0, 6) :
			pg.draw.line(self.window, (255, 255, 255), ((x + 0.5) * 125, 0), ((x + 0.5) * 125, 900))

		if self.mode == 'recording' :
			for note in self.notes :
				pg.draw.circle(self.window, (255, 255, 255), ((note['side']) * 125, note['y']), 60)
				note['y'] += 5

		if self.mode == 'edit' :
			for note in self.notes :
				pg.draw.circle(self.window, (255, 255, 255), ((note['side']) * 125, note['y']), 60)

		#### refresh
		self.clock.tick(self.fps)
		pg.display.flip()


	def run (self) :
		self.onStart()

		self.running = 1
		while self.running :
			for event in pg.event.get() :
				if event.type == pg.QUIT :
					self.running = 0

				elif event.type == pg.KEYDOWN :
					if event.key == pg.K_d : self.notes.append({'time': self.time-185, 'side': 1, 'y': 0})
					if event.key == pg.K_f : self.notes.append({'time': self.time-185, 'side': 2, 'y': 0})
					if event.key == pg.K_j : self.notes.append({'time': self.time-185, 'side': 3, 'y': 0})
					if event.key == pg.K_k : self.notes.append({'time': self.time-185, 'side': 4, 'y': 0})

					elif event.key == pg.K_TAB :
						if self.mode == 'edit' :
							self.mode = 'recording'
							pg.mixer.music.play(start=(self.time/60)/15)

						elif self.mode == 'recording' :
							self.mode = 'edit'
							pg.mixer.music.stop()

				elif event.type == pg.MOUSEWHEEL and self.mode == 'edit' :
					self.time += event.y * 25
					for note in self.notes : note['y'] += event.y * 35

					pg.mixer.music.stop()
					pg.mixer.music.play(start=self.time)

			self.update()
			self.render()

		pg.mixer.quit()
		pg.font.quit()
		pg.quit()

		self.onExit()


	def onStart (self) :
		self.notes = []
		self.time = 0

		self.mode = 'edit'

		pg.mixer.music.load('song/music.mp3')
		pg.mixer.music.play(start=self.time)
		pg.mixer.music.pause()


	def onExit (self) :
		[print(str(note).replace('\'', '"')) for note in self.notes]



if __name__ == '__main__' :
	Game().run()