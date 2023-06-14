from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("Attribute Label Pack")

# Important Label Options
# text - adds the text
# bg - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text =''' निकोला टेस्ला का जन्म 10 जुलाई 1856 को स्किमडज़,
                    \n क्रोएरिया में हुआ था, जब क्रोएशिया अस्ट्रो-हेटेली साम्राज्य का हिस्सा था।
                    \n क्रोएशिया दुनिया में 18 वां सबसे पसंदीदा पर्यटन स्थल है, जो यूरोप का एक देश है। 
                    \n लेकिन जैसा कि हम सभी जानते हैं, आज 161 साल पहले, 
                    \n हमने दुनिया में ज्यादा प्रगति नहीं की थी और उस समय क्रोएरिया (स्मिल्ज़ान), 
                    \n जो निकोला टेस्ला का जन्मस्थान था, गरीब देशों में से एक था।
                    \nनिकोल टेस्ला रोमन कैथोलिक घर में पैदा हुआ था, वह अपने माता-पिता के चौथे बच्चे थे। 
                    \n उनके एक बड़े भाई, डेन, दो बड़ी बहनों, एंजिनिया और मिल्का और एक छोटी बहन, मारिका थी। 
                    \n उनके पिता एक सच्चे रूढ़िवादी चर्च में एक पादरी थे, और यह भी एक कारण था कि 
                    \n उस समय के युवा लोगों के सामने बहुत अधिक रास्ते नहीं थे।
                    ''',
                    bg="black",fg="white",padx=11,pady=13,font="commicsansms 11 bold",
                    borderwidth=5,relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


