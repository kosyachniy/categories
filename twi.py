from func import *

delete('twits')

if __name__=='__main__':
	k=0
	#Создаются лишние строки
	for i in tweepy.Cursor(api.user_timeline, id=mas[ii][0]).items():
		if not i.is_quote_status and not i.in_reply_to_user_id and not i.in_reply_to_status_id:
			mood=stock(i.created_at)
			try:
				write([mood]+text(re.sub(r'https://t.co/\w+$', '', re.sub(r'https://t.co/\w+ ', '', i.text))), name='twits', typ='a')
			except:
				print('Error in tweet №{}'.format(i.id))
			else:
				k+=1
				print(k, mood)
			time.sleep(1)