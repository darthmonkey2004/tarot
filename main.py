import json
from cards_data import *
import PySimpleGUI as sg
from random import shuffle as random_shuffle
from random import randint
import os
import subprocess

txt = """TODO:
Change tarot class to load tarot/tarot_cards/images.data (move out of sub directories into relative root)
Reconfigure update and other image handlers to use dictionary instead of list, organized by 'major' and 'minor' arcanas and 'revesed' and 'normal' orientations.
"""
print(txt)

class tarot():
	def __init__(self, spread_count=3, can_reverse=False):
		self.cards = None
		self.spread_count = spread_count
		self.can_reverse = can_reverse
		self.output = None
		self.back_img = None
		self.card1_clicked = False
		self.card2_clicked = False
		self.card3_clicked = False
		self.card1 = None
		self.card2 = None
		self.card3 = None
		self.reset = False
		self.back_img, self.images = self.read_card_data()

#	def get_files(self, com):
#		return subprocess.check_output(com, shell=True).decode().strip().splitlines()


	def read_card_data(self, path='/home/monkey/tarot'):
		fpath = os.path.join(path, "images.dat")
		with open(fpath, 'r') as f:
			images = json.loads(f.read())
			f.close()
		self.back_img = images['back_img']
		del images['back_img']
		self.images = images
		return self.back_img, self.images


#	def get_card_images(self, path='/home/monkey/tarot/tarot_cards'):
#		major_path = os.path.join(path, 'major_arcana')
#		minor_path = os.path.join(path, 'minor_arcana')
#		out = {}
#		back_img = os.path.join(path, 'back.png')
#		out['major_arcana'] = {}
#		out['minor_arcana'] = {}
#		out['major_arcana']['normal'] = []
#		out['major_arcana']['reversed'] = []
#		out['minor_arcana']['normal'] = []
#		out['minor_arcana']['reversed'] = []
#		com = f"find \"{major_path}\" -name \"*.png\" | grep \"reversed\""
#		out['major_arcana']['reversed'] = self.get_files(com)
#		com = f"find \"{minor_path}\" -name \"*.png\" | grep \"reversed\""
#		out['minor_arcana']['reversed'] = self.get_files(com)
#		com = f"find \"{minor_path}\" -name \"*.png\" | grep -v \"reversed\""
#		out['minor_arcana']['normal'] = self.get_files(com)
#		com = f"find \"{major_path}\" -name \"*.png\" | grep -v \"reversed\""
#		out['major_arcana']['normal'] = self.get_files(com)
#		return back_img, out

	def get_cards(self):
		self.cards = init_cards()
		for arcana in self.images:
			for card_name in self.images[arcana]['normal']:
				self.cards[card_name]['images'] = {}
				self.cards[card_name]['images']['normal'] = self.images[arcana]['normal'][card_name]
			for card_name in self.images[arcana]['reversed']:
				images_key = card_name
				if '.Reversed' in card_name:
					card_name = card_name.split('.')[0]
				self.cards[card_name]['images']['reversed'] = self.images[arcana]['reversed'][images_key]	
		return self.cards



	def shuffle(self, l, count=3):
		for i in range(count):
			random_shuffle(l)
		return l

	def is_reversed(self, range=1024, weight=5):
		num = randint(1, range)
		if num % weight == 0:
			return True
		else:
			return False

	def get_spread(self, spread_count=3, can_reverse=False):
		self.spread_count = spread_count
		self.can_reverse = can_reverse
		cards = self.get_cards()
		names = list(cards.keys())
		out = []
		for i in range(1, spread_count + 1):
			spread_data = {}
			names = self.shuffle(names)
			name = names.pop(0)
			spread_data['name'] = {}
			if self.can_reverse:
				rev = self.is_reversed()
			else:
				rev = False
			spread_data['reversed'] = rev
			if rev:
				try:
					spread_data['front_img'] = cards[name]['images']['reversed']
					#print("Front image:", spread_data['front_img'])
					spread_data['meaning'] = cards[name]['meanings']['reversed']
				except Exception as e:
					print("error!", e, name, rev)
					input()
			else:
				try:
					spread_data['front_img'] = cards[name]['images']['normal']
					#print("Front image:", spread_data['front_img'])
					spread_data['meaning'] = cards[name]['meanings']['normal']
				except Exception as e:
					print("error!", e, name, rev)
					input()
			spread_data['back_img'] = self.back_img
			spread_data['name'] = cards[name]['name']
			spread_data['number'] = cards[name]['number']
			spread_data['number_meaning'] = cards[name]['number_meaning']
			out.append(spread_data)
		return out

	def new(self, spread_count=None, can_reverse=None):
		self.get_dims()
		self.reset = True
		self.win.close()
		self.card1_clicked = False
		self.card2_clicked = False
		self.card3_clicked = False
		if spread_count is not None:
			self.spread_count = spread_count
		if can_reverse is not None:
			self.can_reverse = can_reverse
		self.spread = self.get_spread(spread_count=self.spread_count, can_reverse=self.can_reverse)
		self.win['-CARD_1-'].metadata = self.spread[0]
		self.win['-CARD_2-'].metadata = self.spread[1]
		self.win['-CARD_3-'].metadata = self.spread[2]
		self.card1 = self.win['-CARD_1-'].metadata
		self.card2 = self.win['-CARD_2-'].metadata
		self.card3 = self.win['-CARD_3-'].metadata
		self.win = self.gui()
		self.apply_dims()
		return self.win

	def get_dims(self):
		self.size = self.win.size
		self.location = self.win.current_location()

	def apply_dims(self):
		self.win.size = self.size
		x, y = self.location
		self.win.move(x, y)

	def gui(self):
		spread = self.get_spread(spread_count=self.spread_count, can_reverse=self.can_reverse)
		self.back_img = spread[0]['back_img']
		layout = []
		options = [sg.Checkbox('Enable Random Card Reversal:', default=self.can_reverse, change_submits=True, enable_events=True, key='-CAN_REVERSE-'), sg.Button('New!', key='-NEW_CARDS-'), sg.Button('Exit', key='-EXIT-')]
		layout.append(options)
		spread_line = []
		for card_num in range(1, self.spread_count + 1):
			card = sg.Image(data=self.back_img, key=f"-CARD_{card_num}-", enable_events=True, metadata=spread[card_num - 1])
			spread_line.append(card)
		layout.append(spread_line)
		output = [sg.Text('Select a card to view output!', key='-OUTPUT-', expand_y=True)]
		layout.append(output)
		self.win = sg.Window(title=f"Tarot: {self.spread_count} card spread", layout=layout, finalize=True)
		return self.win

	def update(self):
		self.card1 = self.win['-CARD_1-'].metadata
		self.card2 = self.win['-CARD_2-'].metadata
		self.card3 = self.win['-CARD_3-'].metadata
		if not self.card1_clicked:
			self.win['-CARD_1-'].update(data=self.card1['back_img'])
		else:
			self.win['-CARD_1-'].update(data=self.card1['front_img'])
		if not self.card2_clicked:
			self.win['-CARD_2-'].update(data=self.card2['back_img'])
		else:
			self.win['-CARD_2-'].update(data=self.card2['front_img'])
		if not self.card3_clicked:
			self.win['-CARD_3-'].update(data=self.card3['back_img'])
		else:
			self.win['-CARD_3-'].update(data=self.card3['front_img'])

	def card_onClick(self, key):
		card_data = self.win[key].metadata
		num = int(key.split('-CARD_')[1].split('-')[0])
		if num == 1:
			self.card1 = card_data
			self.card1_clicked = True
		elif num == 2:
			self.card2 = card_data
			self.card2_clicked = True
		elif num == 3:
			self.card3 = card_data
			self.card3_clicked = True
		out = self.parse_output(card_data)
		self.win['-OUTPUT-'].update(out)
		self.update()


	def parse_output(self, card_data):
		lines = []
		lines.append(f"Name: {card_data['name']}")
		lines.append(f"Reversed: {card_data['reversed']}")
		number = card_data['number']
		if number >= 11:
			n1 = int(str(number)[:1])
			n2 = int(str(number)[1:])
			num = n1 + n2
			number = f"{number} ({n1}+{n2}={num})"
		lines.append(f"Numerology number: {number}")
		lines.append("")
		lines.append("Card Meaning:")
		card_meaning = card_data['meaning']
		print("card meaning length:", len(card_meaning))
		if len(card_meaning) > 160:
			l = []
			l.append(card_meaning[:160])
			remainder = card_meaning[160:]
			if len(remainder) > 160:
				l.append(remainder[:160])
				l.append(remainder[160:])
			else:
				l.append(remainder)
			card_meaning = "\n".join(l)
		lines.append(card_meaning)
		lines.append("")
		lines.append("Numerology Meaning:")
		num_meaning = card_data['number_meaning']
		positive = num_meaning.split('Negatively, ')[0]
		try:
			negative = num_meaning.split('Negatively, ')[1]
		except:
			negative = 'No negatives!'
		if card_data['reversed']:
			lines.append(negative)
		else:
			lines.append(positive)
		self.output = "\n".join(lines)
		return self.output
	

def read_loop(t, win):
	while True:
		if win.was_closed():
			if not t.reset:
				print("Exiting...")
				break
			else:
				print("Turning reset off...")
				t.reset = False
		event, values = win.read(timeout=1)
		if event != '__TIMEOUT__':
			if event is None:
				pass
			elif '-CARD_' in event:
				t.card_onClick(event)
			elif event == '-NEW_CARDS-':
				print("TODO: Finish new deal function!")
				win = t.new()
				
			elif event == '-EXIT-':
				t.reset = False
				win.close()
				break
			elif event == '-CAN_REVERSE-':
				t.can_reverse = values[event]
				print("Toggled random card reversal:", t.can_reverse)


if __name__ == "__main__":
	t = tarot()
	win = t.gui()
	read_loop(t, win)
