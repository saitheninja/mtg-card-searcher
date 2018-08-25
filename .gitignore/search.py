from urllib.parse import urlencode
import webbrowser

mydict = {'': 'Gisela, Blade of Goldnight'}

luckshack = "http://luckshack.co.za/index.php?main_page=advanced_search_result&search_in_description=1&keyword"
topdeck = "http://store.topdecksa.co.za/search?q"
sadrobot = "https://sadrobot.co.za/?s"


lssearch = luckshack + urlencode(mydict)
tdsearch = topdeck + urlencode(mydict) + "*"
srsearch = sadrobot + urlencode(mydict) + "&post_type=product"

webbrowser.open_new_tab(lssearch)
webbrowser.open_new_tab(tdsearch)
webbrowser.open_new_tab(srsearch)