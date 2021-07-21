import re
mystr ='''Yeah just one, day one night

Haruman naege sigani itdamyeon
Dalkomhan ni hyanggie chwihaeseo
Gonhi nan jamdeulgopa
Ppakppakhan seukejul saie gihoega itdamyeon
Ttaseuhago gipeun nun ane mom damgeugopa
I like that, neoui geu gilgo gin saengmeori
Ollyeo mukkeul ddaeui ajjilhan
Mokseongwa heulleonaerin janmeori
Seoro gati eodil gadeun
Nae haendeubaegeun ni heori
Yo ma honey bol ttaemada sumi makhyeo
Myeongdong georicheoreom
Uriui bgm-eun sumsori
Nae ireumeul bulleojul ttaeui ni moksorie
Jamgyeoseo nan suyeonghagopa
Neoreul jom deo algopa
Neoran mijiui supeul gipi moheomhaneun tamheomga
Neoran jakpume daehae gamsangeul hae
Neoran jonjaega yesurinikka
Ireohge maeil nan bamsaedorok sangsangeul hae
Eochapi naegeneun muuimihan kkuminikka'''
patt= re.compile(r'like')
matches = patt.finditer(mystr)
for match in matches:
    print(match)