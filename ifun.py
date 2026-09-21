import random


def fortune_cookie():
	fortunes = [
		"A bug is just a feature wearing a disguise.",
		"Today is a great day to refactor something.",
		"Your next idea will compile on the first try!",
		"The rubber duck knows more than it lets on.",
	]
	print("🥠", random.choice(fortunes))


if __name__ == "__main__":
	fortune_cookie()
