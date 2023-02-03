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
			self.time += 1

			keys = pg.key.get_pressed()

			if keys[pg.K_LCTRL] :
				if keys[pg.K_s] : self.saveSong()
				if keys[pg.K_o] : self.openSong()

			if keys[pg.K_d] : self.notes.append({'time': self.time-185, 'side': 1})
			if keys[pg.K_f] : self.notes.append({'time': self.time-185, 'side': 2})
			if keys[pg.K_j] : self.notes.append({'time': self.time-185, 'side': 3})
			if keys[pg.K_k] : self.notes.append({'time': self.time-185, 'side': 4})

			if keys[pg.K_ESCAPE] : self.running = 0


	def render (self) :
		self.window.fill((0, 0, 0))
		#### render

		if self.mode == 'recording' :
			for note in self.notes :
				pass # render notes

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

				if event.type == pg.KEYDOWN :
					if event.key == pg.K_TAB and self.mode == 'edit'      : self.mode = 'recording'
					if event.key == pg.K_TAB and self.mode == 'recording' : self.mode = 'edit'

			self.update()
			self.render()

		pg.mixer.quit()
		pg.font.quit()
		pg.quit()

		self.onExit()


	def onStart (self) :
		self.notes = []
		self.time = 0

		self.mode = 'recording'


	def onExit (self) :
		[print(note) for note in self.notes]



if __name__ == '__main__' :
	Game().run()