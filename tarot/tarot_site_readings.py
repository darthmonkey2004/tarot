from selenium import webdriver
from selenium.webdriver import ChromeOptions
from urllib.parse import unquote
from bs4 import BeautifulSoup as bs

nums = {0: {'alpha': 'Zero', 'description': '0 is the Alpha (beginning) and Omega (the highest) as there is no beginning and no end; all is infinite. \nThe ancients proclaimed that the ‘God force’ is a circle whose centre is everywhere and its circumference is nowhere. \nZero is the symbol of ‘nothingness’ and denotes freedom from limitations in this material world. \nZero is the number of the ‘God’ force and Universal Energies and reinforces, amplifies and magnifies the vibrations of the numbers it appears with. \nThe number zero encompasses the attributes of all other numbers, and brings one closer to the ‘God force’ or ‘Source’. \nNumber zero resonates with the vibrations and energies of eternity, infinity, oneness, wholeness, continuing cycles and flow, and the beginning point. \nNumber 0 stands for potential and/or choice, and when this number presents and recurs it is a message to do with developing one’s spiritual aspects as \nzero is considered to represent the beginning of a spiritual journey and highlights the uncertainties that may entail. \nIt suggests that you listen to your intuition and higher-self as this is where you will find all of your answers.', 'attributes': {'positive': ['alpha/omega', 'infinite', 'God force', 'nothingness', 'freedom from limitations', 'freedom from material posessions', 'Universal Energies', 'all encompassing', 'Source', 'eternity', 'infinity', 'oneness', 'wholeness', 'continuing cycles and flow', 'beginning point'], 'negative': []}, 'properties': ['amplifier']}, 1: {'alpha': 'One', 'description': 'Number 1 resonates with the vibrations and attributes of new beginnings, creation, independence, uniqueness, motivation, striving forward and progress, ambition\nand will power, positivity and positiveness, the energies of pioneering, raw energy, force, activity, self-leadership and assertiveness, initiative, instinct and intuition,\nthe masculine attributes, organization, achievement and success, strength and self-reliance, tenacity, forcefulness and authority, love, inspiration, attainment,\nglory, happiness, fame, fulfilment and omniscience, and creating your own realities.\nNegatively, number 1 relates to single-mindedness, intolerance, conceit, narrow-mindedness, lacking in emotion and being weak-willed, dependence, passivity, aggression,\narrogance and dominance.', 'attributes': {'positive': ['new beginnings', 'creation', 'independence', 'uniqueness', 'motivation', 'striving forward and progress', 'ambition and will power', 'positivity and positiveness', 'the energies of pioneering', 'raw energy', 'force', 'activity', 'self-leadership and assertiveness', 'initiative', 'instinct and intuition', 'the masculine attributes', 'organization', 'achievement and success', 'strength and self-reliance', 'tenacity', 'forcefulness and authority', 'love', 'inspiration', 'attainment', 'glory', 'happiness', 'fame', 'fulfilment and omniscience', 'creating your own realities'], 'negative': ['single-mindedness', 'intolerance', 'conceit', 'narrow-mindedness', 'lacking in emotion and being weak-willed', 'dependence', 'passivity', 'aggression', 'arrogance and dominance.']}, 'properties': []}, 2: {'alpha': 'Two', 'description': 'Number 2 resonates with the vibrations of service and duty, balance and harmony, adaptability, diplomacy, charm, co-operation, consideration, friendliness,\nreceptivity and love, understanding, personal will, the peacemaker, gentleness and kindness, art, insightfulness, ambition, sensitivity, placidity, just and justice,\nselflessness, sociability and support, attention to detail, decisiveness, poise, intuition, caution, flexibility, grace, devotion, mediation, partnerships and relationships,\nencouragement, happiness and musical rhythm, faith and trust and serving and living your Divine life purpose and soul mission.\nNegatively, number 2 resonates with indifference, the inability to take responsibility, fearfulness, pessimism, dependency, indecisiveness, hesitation, lack of balance,\ninstability and irresoluteness, insensitivity, inflexibility, stagnation, a lack of consideration, unemotional and unloving, argumentative and disagreeability,\nfears such as the fear of unplanned changes, of making mistakes, of being alone and the fear of the unknown.', 'attributes': {'positive': ['service and duty', 'balance and harmony', 'adaptability', 'diplomacy', 'charm', 'co-operation', 'consideration', 'friendliness', 'receptivity and love', 'understanding', 'personal will', 'the peacemaker', 'gentleness and kindness', 'art', 'insightfulness', 'ambition', 'sensitivity', 'placidity', 'just and justice', 'selflessness', 'sociability and support', 'attention to detail', 'decisiveness', 'poise', 'intuition', 'caution', 'flexibility', 'grace', 'devotion', 'mediation', 'partnerships and relationships', 'encouragement', 'happiness and musical rhythm', 'faith/trust', 'Divine life purpose', 'soul mission'], 'negative': ['indifference', 'the inability to take responsibility', 'fearfulness', 'pessimism', 'dependency', 'indecisiveness', 'hesitation', 'lack of balance', 'instability and irresoluteness', 'insensitivity', 'inflexibility', 'stagnation', 'a lack of consideration', 'unemotional and unloving', 'argumentative and disagreeability', 'fears such as the fear of unplanned changes', 'fear of making mistakes', 'fear of being alone', 'fear of the unknown']}}, 3: {'alpha': 'Three', 'description': 'Number 3 resonates with the energies of optimism and joy, inspiration and creativity, speech and communication, good taste, imagination and intelligence,\nsociability and society, friendliness, kindness and compassion, art, humour, energy, growth, expansion and the principles of increase, spontaneity, broad-minded thinking,\nencouragement, assistance, talent and skills, culture, wit, a love of fun and pleasure, freedom-seeking, adventure, exuberance, brilliance, free-form, being brave,\nnon-confrontational, free-form, rhythm, passion, surprise, sensitivity, self-expression, affability, enthusiasm, youthfulness, enlivenment, psychic ability,\nmanifesting and manifestation. Number 3 resonates with the energies of the Ascended Masters, and indicates that the Ascended Masters are around you, assisting when asked. \nThe Ascended Masters help you to focus upon the Divine spark within yourself and others, and assist with manifesting your desires.\nThey are helping you to find peace, clarity and love within. \nNegatively, number 3 relates to indifference, a lack of stamina and concentration, a spectacular rise and fall, mood swings and mania.', 'attributes': {'positive': ['optimism and joy', 'inspiration and creativity', 'speech and communication', 'good taste', 'imagination and intelligence', 'sociability and society', 'friendliness', 'kindness and compassion', 'art', 'humour', 'energy', 'growth', 'expansion and the principles of increase', 'spontaneity', 'broad-minded thinking', 'encouragement', 'assistance', 'talent and skills', 'culture', 'wit', 'a love of fun and pleasure', 'freedom-seeking', 'adventure', 'exuberance', 'brilliance', 'free-form', 'being brave', 'non-confrontational', 'free-form', 'rhythm', 'passion', 'surprise', 'sensitivity', 'self-expression', 'affability', 'enthusiasm', 'youthfulness', 'enlivenment', 'psychic ability'], 'negative': ['indifference', 'lack of stamina and concentration', 'spectacular rise and fall', 'mood swings', 'mania']}, 'properties': ['Ascended Masters', 'Divine Aid']}, 4: {'alpha': 'Four', 'description': 'Number 4 resonates with the vibrations and energies of practicality, organization and exactitude, service, patience, devotion, application, pragmatism, patriotism,\ndignity, trust and trust-worthiness, endurance, loyalty, mastery, building solid foundations, conservatism, determination, production and hard work, high morals,\ntraditional values, honesty and integrity, inner-wisdom, security, self-control, loyalty, conscientiousness, reality and realistic values, stability and ability,\nprogress, management, justice, seriousness, discipline, system and order, maintenance, constructiveness, dependability, conviction, passion and drive.\nNumber 4 also resonates with the energies of the Archangels.\nNegativity, number 4 relates to a lack of convention and conviction, the inability to adapt, clumsiness, laziness and dullness.', 'attributes': {'positive': ['practicality', 'organization and exactitude', 'service', 'patience', 'devotion', 'application', 'pragmatism', 'patriotism', 'dignity', 'trust and trust-worthiness', 'endurance', 'loyalty', 'mastery', 'building solid foundations', 'conservatism', 'determination', 'production and hard work', 'high morals', 'traditional values', 'honesty and integrity', 'inner-wisdom', 'security', 'self-control', 'loyalty', 'conscientiousness', 'reality and realistic values', 'stability and ability', 'progress', 'management', 'justice', 'seriousness', 'discipline', 'system and order', 'maintenance', 'constructiveness', 'dependability', 'conviction', 'passion', 'drive'], 'negative': ['convention and conviction', 'the inability to adapt', 'clumsiness', 'laziness', 'dullness']}, 'properties': ['Archangels']}, 5: {'alpha': 'Five', 'description': 'Number 5 resonates with the influences and attributes of personal freedom, the unconventional, individualism, non-attachment, change,\nlife lessons learned through experience, variety, adaptability and versatility, resourcefulness, motivation, progress, activity, experience, travel and adventure,\nsympathy and understanding, sociability and companionability, release and surrender, influence, sensuality, promotion, natural flair,  vivacious,\ncourage and being courageous, health and healing, idealism, telepathy, pleasure-seeking and pleasure loving, vitality, vision and the visionary, expansion, opportunity,\nstory-telling, mercy, kindness, invention, magnetism, competitiveness, imagination, curiosity, cleverness and intelligence, and making life choices and decisions.\nNegatively, number 5 relates to being rash and irresponsible, inconsistent, unreliability, thoughtlessness, non-committal, fear of change, rigid in thought and action,\na lack of vitality, a dislike of confinement and routine, restlessness, inactivity and stagnation, upheaval and discord.', 'attributes': {'positive': ['personal freedom', 'the unconventional', 'individualism', 'non-attachment', 'change', 'life lessons learned through experience', 'variety', 'adaptability and versatility', 'resourcefulness', 'motivation', 'progress', 'activity', 'experience', 'travel and adventure', 'sympathy and understanding', 'sociability and companionability', 'release and surrender', 'influence', 'sensuality', 'promotion', 'natural flair', ' vivacious', 'courage and being courageous', 'health and healing', 'idealism', 'telepathy', 'pleasure-seeking and pleasure loving', 'vitality', 'vision and the visionary', 'expansion', 'opportunity', 'story-telling', 'mercy', 'kindness', 'invention', 'magnetism', 'competitiveness', 'imagination', 'curiosity', 'cleverness and intelligence', 'making life choices and decisions'], 'negative': ['rashness', 'irresponsibility', 'inconsistent', 'unreliability', 'thoughtlessness', 'non-committal', 'fear of change', 'rigid in thought and action', 'lack of vitality', 'dislike of confinement', 'dislike of routine', 'restlessness', 'inactivity', 'stagnation', 'upheaval', 'discord']}, 'properties': []}, 6: {'alpha': 'Six', 'description': 'Number 6 is related to the vibrations and energies of unconditional love, balance and harmony, home and family, domesticity, parenthood, guardianship, service to others,\nselflessness, responsibility, nurturing, care, empathy and sympathy, self-sacrifice, humanitarianism, the ability to compromise, emotional depth, honesty and integrity,\nadjustment, stability, poise, protection, firmness, healing, idealism, just and justice, conscientiousness, burden-fearing, solution-finding, problem-solving,\nseeing clearly, teaching, convention, curiosity, peace and peacefulness, circulation, grace and dignity, simplicity, reliability, material needs and economy,\nproviding and provision, agriculture and growth, musical talent.\nThe negative aspects of number 6 are weakness and being weak-willed, a superiority complex, impracticality, shallowness, submissiveness, restlessness, unsupportiveness,\nselfishness and being easily stressed.', 'attributes': {'positive': ['unconditional love', 'balance and harmony', 'home and family', 'domesticity', 'parenthood', 'guardianship', 'service to others', 'selflessness', 'responsibility', 'nurturing', 'care', 'empathy and sympathy', 'self-sacrifice', 'humanitarianism', 'the ability to compromise', 'emotional depth', 'honesty', 'integrity', 'adjustment', 'stability', 'poise', 'protection', 'firmness', 'healing', 'idealism', 'just and justice', 'conscientiousness', 'burden-fearing', 'solution-finding', 'problem-solving', 'seeing clearly', 'teaching', 'convention', 'curiosity', 'peace', 'circulation', 'grace', 'dignity', 'simplicity', 'reliability', 'material needs', 'economy', 'providing', 'provisions', 'agriculture', 'growth', 'musical talent'], 'negative': ['weakness', 'weak-willed', 'superiority complex', 'impracticality', 'shallowness', 'submissiveness', 'restlessness', 'unsupportiveness', 'selfishness', 'easily stressed']}, 'properties': []}, 7: {'alpha': 'Seven', 'description': 'Number 7 resonates with the vibrations and energies of the ‘Collective Consciousness’, faith and spirituality, spiritual awakening and awareness, spiritual enlightenment,\nspiritual acceptance and development, mysticism, intuition and inner-knowing, inner-wisdom, psychic abilities, the esoteric, inner-selves, deep contemplation, introspection,\neccentric, religion, thoughtfulness, understanding of others, natural healer and healing, secrets, myth, ritual, peace, poise, emotions and feelings, inner-strength,\nendurance and perseverance, persistence of purpose, the ability to bear hardships, quick-wit, the loner, solitary,  isolation, long-sighted, the non-conformist,\nindependence and individualism, intentions, manifesting and manifestation in time and space, good fortune, mental analysis, philosophy and the philosophical, technicality,\nscientific research, science, alchemy, genius, a keen mind, specialising and the specialist, the inventor, determination, the written word, logic, understanding,\ndiscernment and discerning, knowledge-seeking, study, education and learning, writing and the writer, evolution, stability, the ability to set limits, completion,\nrefinement, stoicism, silence, perfection, chastity, dignity, ascetic, rigor, ahead of the times.\nNegatively, the vibrations of the number 7 are morbidity and depression, inactivity, hypercritical, anti-social, pessimistic, dependency and co-dependency,\nstagnation, lack of persistence, pride, narrow-mindedness, distance, arguments and being argumentative, misanthropic, resentment and being resentful, self-righteousness,\nunwilling and/or unable to share ideas and compromise, limitations and silence.', 'attributes': {'positive': ['Collective Consciousness', 'faith and spirituality', 'spiritual awakening and awareness', 'spiritual enlightenment', 'spiritual acceptance and development', 'mysticism', 'intuition and inner-knowing', 'inner-wisdom', 'psychic abilities', 'the esoteric', 'inner-selves', 'deep contemplation', 'introspection', 'eccentric', 'religion', 'thoughtfulness', 'understanding of others', 'natural healer and healing', 'secrets', 'myth', 'ritual', 'peace', 'poise', 'emotions and feelings', 'inner-strength', 'endurance and perseverance', 'persistence of purpose', 'the ability to bear hardships', 'quick-wit', 'the loner', 'solitary', ' isolation', 'long-sighted', 'the non-conformist', 'independence and individualism', 'intentions', 'manifesting and manifestation in time and space', 'good fortune', 'mental analysis', 'philosophy and the philosophical', 'technicality', 'scientific research', 'science', 'alchemy', 'genius', 'a keen mind', 'specialising and the specialist', 'the inventor', 'determination', 'the written word', 'logic', 'understanding', 'discernment and discerning', 'knowledge-seeking', 'study', 'education and learning', 'writing and the writer', 'evolution', 'stability', 'the ability to set limits', 'completion', 'refinement', 'stoicism', 'silence', 'perfection', 'chastity', 'dignity', 'ascetic', 'rigor', 'ahead of the times'], 'negative': ['morbidity', 'depression', 'inactivity', 'hypercritical', 'anti-social', 'pessimistic', 'dependency', 'co-dependency', 'stagnation', 'lack of persistence', 'pride', 'narrow-mindedness', 'distance', 'argumentative', 'misanthropic', 'resentment and being resentful', 'self-righteousness', 'unwilling and/or unable to share ideas and compromise', 'limitations', 'silence']}, 'properties': []}, 8: {'alpha': 'Eight', 'description': 'Number 8 resonates with the influences and vibrations of authority and personal power, self-confidence, executive ability, confidence, inner-strength,\nprofessionalism and the professional, management, material freedom, success, good judgement, money, finances, riches, manifesting wealth, abundance and prosperity,\nprovision, investments, discrimination and discernment, giving and receiving, thoroughness, dependability, self-reliance, repose, practicality, consideration,\ninner-wisdom, self-sufficiency, social status, pragmatism, the ego, aggregation, compassion, dictatorship, executive, delegation, reality, truth and integrity,\ncompassion, dictatorship, multiples, employment, stability, appearance, customs, skills and talents, exchanges, truth, good judgement and problem-solving,\norganisation and organizing, achieving and achievements, decisiveness, control, constant, ambition, the authoritarian, challenge, efficiency, trustworthiness,\ninsight, planning and the planner, sociability, works independently, learning through experience, true justice, retreat, patience, caution, self-discipline, free-will,\ninsight, spiritual consciousness, a desire for peace and a love of humanity and world transformation.\nThe negative aspects of number 8 are a superiority complex, greed, tactlessness and domineering.\nNumber 8 is the number of Karma – the Universal Spiritual Law of Cause and Effect.', 'attributes': {'positive': ['authority', 'personal power', 'self-confidence', 'executive ability', 'confidence', 'inner-strength', 'professionalism', 'the professional', 'management', 'material freedom', 'success', 'good judgement', 'money', 'finances', 'riches', 'manifesting wealth', 'abundance', 'prosperity', 'provision', 'investments', 'discrimination', 'discernment', 'giving', 'receiving', 'thoroughness', 'dependability', 'self-reliance', 'repose', 'practicality', 'consideration', 'inner-wisdom', 'self-sufficiency', 'social status', 'pragmatism', 'the ego', 'aggregation', 'compassion', 'dictatorship', 'executive', 'delegation', 'reality', 'truth', 'integrity', 'compassion', 'dictatorship', 'multiples', 'employment', 'stability', 'appearance', 'customs', 'skills', 'talents', 'exchanges', 'truth', 'good judgement', 'problem-solving', 'organisation', 'organizing', 'achieving', 'achievements', 'decisiveness', 'control', 'constant', 'ambition', 'the authoritarian', 'challenge', 'efficiency', 'trustworthiness', 'insight', 'planning', 'the planner', 'sociability', 'works independently', 'learning through experience', 'true justice', 'retreat', 'patience', 'caution', 'self-discipline', 'free-will', 'insight', 'spiritual consciousness', 'a desire for peace', 'a love of humanity', 'world transformation.'], 'negative': ['superiority complex', 'greed', 'tactlessness', 'domineering']}, 'properties': ['Karma', 'the Universal Spiritual Law of Cause and Effect.']}, 9: {'alpha': 'Nine', 'description': 'Number 9 is the number of Universal love, eternity, faith, Universal Spiritual Laws, karma, spiritual enlightenment, spiritual awakening, service to humanity,\nhumanitarianism and the humanitarian, lightworking and lightworkers, leading by positive example, philanthropy and the philanthropist, charity, self-sacrifice,\nselflessness, destiny, soul purpose and mission, generosity, a higher perspective, romance, inner-strength, public relations, responsibility, intuition,\nstrength of character, learning to say ‘No’, creative abilities, sensitivity, loyalty, generalist, discretion, brilliance, problem-solving, inner-wisdom, self-love,\nfreedom, popularity, high ideals, tolerance, humility, altruism and benevolence, empathy, compassion, non-conformity, artistic genius, an expansive viewpoint,\neccentricity, communication, influence, perfection, magnetism, understanding, forgiveness, compassion and sympathy, the visionary, duty and calling, obligation,\nmysticism, optimism and Divine wisdom.\nNegatively, number 9 relates to disconnection, lethargy and an inability to concentrate and focus.', 'attributes': {'positive': ['Universal love', 'eternity', 'faith', 'Universal Spiritual Laws', 'karma', 'spiritual enlightenment', 'spiritual awakening', 'service to humanity', 'humanitarianism', 'the humanitarian', 'lightworking', 'lightworkers', 'leading by positive example', 'philanthropy', 'the philanthropist', 'charity', 'self-sacrifice', 'selflessness', 'destiny', 'soul purpose', 'mission', 'generosity', 'a higher perspective', 'romance', 'inner-strength', 'public relations', 'responsibility', 'intuition', 'strength of character', 'learning to say ‘No’', 'creative abilities', 'sensitivity', 'loyalty', 'generalist', 'discretion', 'brilliance', 'problem-solving', 'inner-wisdom', 'self-love', 'freedom', 'popularity', 'high ideals', 'tolerance', 'humility', 'altruism', 'benevolence', 'empathy', 'compassion', 'non-conformity', 'artistic genius', 'an expansive viewpoint', 'eccentricity', 'communication', 'influence', 'perfection', 'magnetism', 'understanding', 'forgiveness', 'compassion', 'sympathy', 'the visionary', 'duty', 'calling', 'obligation', 'mysticism', 'optimism', 'Divine wisdom'], 'negative': ['disconnection', 'lethargy', 'inability to concentrate and focus']}, 'properties': []}, 10: {'alpha': 'Ten', 'description': 'Number 10 resonates with the vibrations and energies of leadership, optimism, confidence, independence, creative powers, success, energy, originality,\nadaptability, determination and individuality.\nThe number 10 reduces to the single digit of 1 (1+0=1).', 'attributes': {'positive': ['leadership', 'optimism', 'confidence', 'independence', 'creative powers', 'success', 'energy', 'originality', 'adaptability', 'determination', 'individuality'], 'negative': []}, 'properties': []}}

def get_readings():
	opts = ChromeOptions()
	opts.add_argument('--headless')
	driver = webdriver.Chrome(options=opts)
	url = 'https://www.tarot.com/readings-reports'
	driver.get(url)
	html = bs(driver.page_source, 'html.parser')
	data = unquote(str(html))
	s = '<catalog-products>'
	data = data.split(s)[1].split('<catalog-product>')
	d = {}
	for line in data:
		if 'KARMA COINS' in line:
			price_type = 'paid'
			price = line.split('KARMA COINS')[0].split('/>')[1]
		elif 'FREE' in line:
			price_type = 'free'
			price = 0
		if 'href="' in line:
			url = line.split('href="')[1].split('"')[0]
			img_url = line.split('data-src="')[1].split('"')[0]
			title = line.split('<h3><span>')[1].split('</span>')[0].replace('&amp;', '&')
			d[title] = {}
			d[title]['url'] = url
			d[title]['img_url'] = img_url
			d[title]['title'] = title
			d[title]['price_type'] = price_type
			d[title]['price'] = price
	return d


def set_reading(name=None, price_type='free'):
	data = get_readings()
	if name is None:
		name = 'Free Tarot Reading'
		return data[name]
	elif name == 'all':
		pos = 0
		for name in data.keys():
			if data[name]['price_type'] == price_type:
				pos += 1
				print(f"{pos}. {data[name]['title']}")
		idx = int(input("Enter selection number:"))
		title = list(data.keys())[idx]
		return data[title]


			
if __name__ == "__main__":
	reading = set_reading()
	print(reading)
