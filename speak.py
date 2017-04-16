#!/usr/bin/env python
# *-* coding: utf-8 *-*

import tweepy
from random import choice
from tweepy import OAuthHandler

class Twitterings:
	def __init__(self):
		self.name = 'Jospeh Heller'
		self.auth = OAuthHandler('Bn5Jnz1mf3JXBHAM7XvgbJMnH', 'WSbrPB3N5cIJaHM36LEiUaEywA8k6Zzi89hxoIekjr139pnXV1')
		self.auth.set_access_token('853559235745107968-EXQDyL2bbbsAkof0xW5u2fg08rYwErE', 'fToyRaNywUAe5T4ShSGo6dnDLQfgnkETiE9fOfc2KwG6s' )
		self.api = tweepy.API(self.auth)
		self.me = self.api.me()

	def wonderings(self):
		"""The Maestros words"""

		things = [
		'Some men are born mediocre, some men achieve mediocrity, and some men have mediocrity thrust upon them.',
		'He had decided to live forever or die in the attempt.',
		'The enemy is anybody who is going to get you killed, no matter which side he is on.',
		'Every writer I know has trouble writing.',
		'When I grow up I want to be a little boy.',
		"Destiny is a good thing to accept when it's going your way.",
		"When destiny isn't going your way don't call it destiny; call it injustice, treachery, or simple bad luck.",
		'I want to keep my dreams, even bad ones, because without them, I might have nothing all night long.',
		'He was a self-made man who owed his lack of success to nobody.',
		'He knew everything about literature except how to enjoy it.',
		"Frankly, I'd like to see the government get out of war altogether and leave the whole field to private individuals.",
		"Just because you're paranoid doesn't mean they aren't after you.",
		'Anything worth dying for ... is certainly worth living for.',
		'Insanity is contagious.',
		'They agreed that it was neither possible nor necessary to educate people who never questioned anything.',
		"It doesn't make a damned bit of difference who wins the war to someone who's dead.",
		"It's the best there is, Doc Daneeka agreed.",
		"That's some catch, that Catch-22, he observed.",
		'There was only one catch and that was Catch-22',
		'The Texan turned out to be good-natured, generous and likable. In three days no one could stand him',
		"Be glad you're even alive.  Be furious you're going to die.",
		'I want to keep my dreams, even bad ones, because without them, I might have nothing all night long.',
		'There is no disappointment so numbing...as someone no better than you achieving more.',
		"When I look up, I see people cashing in.  I don't see heaven or saints or angels.",
		"I see people cashing in on every decent impulse and every human tragedy.",
		"Well, he died. You don't get any older than that.",
		'mankind is resilient: the atrocities that horrified us a week ago become acceptable tomorrow.',
		"They're trying to kill me, Yossarian told him calmly.",
		"No one's trying to kill you, Clevinger cried.",
		"They're shooting at everyone, Clevinger answered. They're trying to kill everyone.  And what difference does that make?",
		"Catch-22 specified that a concern for one's safety in the face of dangers that were real and immediate was the process of a rational mind.",
		"All he had to do was ask; and as soon as he did, he would no longer be crazy and would have to fly more missions.",
		"Orr was crazy and could be grounded. Orr would be crazy to fly more missions and sane if he didn't, but if he was sane he had to fly them.",
		"Yossarian was moved very deeply by the absolute simplicity of this clause of Catch-22 and let out a respectful whistle",
		"What is a country? A country is a piece of land surrounded on all sides by boundaries, usually unnatural.",
		"Englishmen are dying for England, Americans are dying for America, Germans are dying for Germany, Russians are dying for Russia.",
		"There are now fifty or sixty countries fighting in this war. Surely so many countries can't all be worth dying for.",
		"What a lousy earth! He wondered how many people were destitute that same night even in his own prosperous country",
		"how many homes were shanties, how many husbands were drunk and wives socked, and how many children were bullied, abused, or abandoned.",
		"How many families hungered for food they could not afford to buy? How many hearts were broken?",
		"How many suicides would take place that same night, how many people would go insane? How many cockroaches and landlords would triumph?",
		"How many winners were losers, successes failures, and rich men poor men? How many wise guys were stupid?",
		"How many happy endings were unhappy endings? How many honest men were liars, brave men cowards, loyal men traitors",
		"how many sainted men were corrupt, how many people in positions of trust had sold their souls to bodyguards",
		"how many had never had souls? How many straight-and-narrow paths were crooked paths?",
		"How many best families were worst families and how many good people were bad people?",
		"It was miraculous. It was almost no trick at all, he saw, to turn vice into virtue and slander into truth",
		"impotence into abstinence, arrogance into humility, plunder into philanthropy, thievery into honor, blasphemy into wisdom",
		"brutality into patriotism, and sadism into justice. Anybody could do it; it required no brains at all. It merely required no character.",
		"Why are they going to disappear him? I don't know. It doesn't make sense. It isn't even good grammar.",
		"Man was matter, that was Snowden's secret. Drop him out a window, and he'll fall. Set fire to him and he'll burn.",
		"Bury him and he'll rot, like other kinds of garbage. The spirit gone, man is garbage. That was Snowden's secret.",
		"The country was in peril; he was jeopardizing his traditional rights of freedom and independence by daring to exercise them.",
		"You have a morbid aversion to dying. You probably resent the fact that you're at war and might get your head blown off any second.",
		"You have deep-seated survival anxieties. And you don't like bigots, bullies, snobs, or hypocrites.",
		"Subconsciously there are many people you hate.",
		"Consciously, sir, consciously, Yossarian corrected in an effort to help. I hate them consciously.",
		"You're antagonistic to the idea of being robbed, exploited, degraded, humiliated, or deceived. Misery depresses you.",
		"Ignorance depresses you. Persecution depresses you. Violence depresses you. Corruption depresses you.",
		"Even among men lacking all distinction he inevitably stood out as a man lacking more distinction than all the rest",
		"People who met him were always impressed by how unimpressive he was.",
		"From now on I'm thinking only of me.",
		"I'd certainly be a damned fool to feel any other way, wouldn't I?",
		"Well, maybe it is true, Clevinger conceded unwillingly in a subdued tone.",
		"There's nothing mysterious about it, He's not working at all. He's playing.",
		"He's forgotten all about us.",
		"Do you know how long a year takes when it's going away?",
		"You're inches away from death every time you go on a mission.",
		"How the hell else are you ever going to slow down?",
		"Maybe a long life does have to be filled with many unpleasant conditions if it's to seem long. But in that event, who wants one?",
		"That's the kind of God you people talk about, a country bumpkin, a clumsy, bungling, brainless, conceited, uncouth hayseed.",
		]

		return things

	def existing(self):

		return [n.text for n in self.api.user_timeline() ]


	def speak(self,text=None):
		"""Post a Quote to Twitter"""

		if text==None:
			current = choice(self.wonderings())
			while current in self.existing():
				current = choice(self.wonderings())
			self.api.update_status(current)
		else:
			self.api.update_status(text)

		return True

	def validate(self):
		"""Reports any snippets that are above 140 characters"""

		for n in self.wonderings():
			if len(n)>139:
				print n

if __name__ == '__main__':
	twitter = Twitterings()
	twitter.speak()
