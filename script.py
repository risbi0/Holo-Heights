from PIL import Image
import os

file_dir = os.path.dirname(__file__)

data = {
    'Airani Iofifteen': 150,
    'Akai Haato': 154,
    'Aki Rosenthal': 162,
    'Amane Kanata': 149,
    'Anya Melfissa': 147,
    'Aragami Oga': 192,
    'Arurandeisu': 184,
    'Astel Leda': 158,
    'Axel Syrios': 184,
    'Ayunda Risu': 153,
    'AZKi': 158,
    'Banzoin Hakka': 174,
    'Ceres Fauna': 164,
    'Fuwawa Abyssgard': 155,
    'Gavis Bettel': 180,
    'Gawr Gura': 141,
    'Hakos Baelz': 149,
    'Hakui Koyori': 153,
    'Hanasaki Miyabi': 174,
    'Himemori Luna': 140,
    'Hiodoshi Ao': 171,
    'Hizaki Gamma': 178,
    'Hoshimachi Suisei': 160,
    'Houshou Marine': 150,
    'Ichijou Ririka': 162,
    'Inugami Korone': 156,
    'IRyS': 166,
    'Josuiji Shinri': 183,
    'Juufuutei Raden': 159,
    'Kaela Kovalskia': 173,
    'Kageyama Shien': 176,
    'Kanade Izuru': 163,
    'Kazama Iroha': 156,
    'Kiryu Coco': 180,
    'Kishido Temma': 179,
    'Kobo Kanaeru': 150,
    'Koseki Bijou': 140,
    'Kureiji Ollie': 162,
    'Laplus Darknesss': 139,
    'Machina X Flayon': 163,
    'Magni Dezmond': 184,
    'Mano Aloe': 150,
    'Minase Rio': 170,
    'Minato Aqua': 148,
    'Mococo Abyssgard': 155,
    'Momosuzu Nene': 159,
    'Moona Hoshinova': 165,
    'Mori Calliope': 167,
    'Murasaki Shion': 145,
    'Nakiri Ayame': 152,
    'Nanashi Mumei': 156,
    'Natsuiro Matsuri': 152,
    'Nekomata Okayu': 152,
    'Nerissa Ravencroft': 175,
    'Ninomae Inanis': 157,
    'Noir Vesper': 189,
    'Omaru Polka': 153,
    'Ookami Mio': 160,
    'Oozora Subaru': 154,
    'Otonose Kanade': 153,
    'Ouro Kronii': 168,
    'Pavolia Reine': 172,
    'Regis Altare': 176,
    'Rikka': 179,
    'Robocosan': 154,
    'Sakamata Chloe': 148,
    'Sakura Miko': 152,
    'Shiori Novella': 163,
    'Shirakami Fubuki': 155,
    'Shiranui Flare': 158,
    'Shirogane Noel': 158,
    'Shishiro Botan': 166,
    'Takanashi Kiara': 165,
    'Takane Lui': 161,
    'Todoroki Hajime': 155,
    'Tokino Sora': 160,
    'Tokoyami Towa': 150,
    'Tsukumo Sana': 169,
    'Tsunomaki Watame': 151,
    'Uruha Rushia': 143,
    'Usada Pekora': 153,
    'Utsugi Uyu': 177,
    'Vestia Zeta': 155,
    'Watson Amelia': 150,
    'Yatogami Fuma': 168,
    'Yozora Mel': 154,
    'Yukihana Lamy': 158,
    'Yukoku Roberu': 181,
    'Yuzuki Choco': 165,
    'Jurard T Rexford': 181,
    'Goldbullet': 190,
    'Octavio': 174,
    'Crimzon Ruze': 184,
    'Aia Amare': 158,
	'Alban Knox': 175,
	'Aster Arcadia': 170,
	'Claude Clawmark': 171,
	'Doppio Dropscythe': 187,
	'Elira Pendora': 160,
	'Finana Ryugu': 140,
	'Fulgur Ovid': 178,
	'Hex Haywire': 185,
	'Ike Eveland': 180,
	'Kotoka Torahime': 166,
	'Kunai Nakasato': 162,
	'Kyo Kaneko': 183,
	'Luca Kaneshiro': 178,
	'Maria Marionette': 152,
	'Meloco Kyoran': 171,
	'Millie Parfait': 150,
	'Mysta Rias': 177,
	'Nina Kosaka': 174,
	'Petra Gurin': 152,
	'Pomu Rainpuff': 156,
	'Reimu Endou': 155,
	'Ren Zotto': 180,
	'Rosemi Lovelock': 150,
	'Scarle Yonaguni': 165,
	'Selen Tatsuki': 160,
	'Shu Yamino': 173,
	'Sonny Brisko': 180,
	'Uki Violeta': 169,
	'Vantacrow Bringer': 182,
	'Ver Vermillion': 175,
	'Vezalius Bandage': 178,
	'Victoria Brightshield': 157,
	'Vox Akuma': 178,
	'Yugo Asuma': 168,
	'Yu Q Wilson': 175,
	'Zaion LanZa': 153,
	'Achikita Chinami': 154,
	'Aiba Uiha': 167,
	'Aizono Manami': 154,
	'Akabane Youko': 160,
	'Akagi Wen': 171,
	'Akira Ray': 155,
	'Amagase Muyu': 167,
	'Amamiya Kokoro': 150,
	'Amemori Sayo': 157,
	'Amicia Michella': 150,
	'Ange Katrina': 160,
	'Ars Almal': 147,
	'Asahina Akane': 158,
	'Asuka Hina': 145,
	'Axia Krone': 179,
	'Azuchi Momo': 154,
	'Azura Cecillia': 171,
	'Ban Hada': 165,
	'Belmond Banderas': 191,
	'Bonnivier Pranaja': 183,
	'Derem Kado': 156,
	'Dola': 170,
	'Eli Conifer': 155,
	'Elu': 170,
	'Emma August': 138,
	'Etna Crimson': 154,
	'Ex Albio': 183,
	'Fumino Tamaki': 157,
	'Fumi': 176,
	'Fura Kanato': 177,
	'Furen E Lustario': 168,
	'Fushimi Gaku': 178,
	'Fuwa Minato': 173,
	'Gaon': 170,
	'Genzuki Tojiro': 183,
	'Gundo Mirei': 175,
	'Gwelu Os Gar': 185,
	'Hakase Fuyuki': 152,
	'Hanabatake Chaika': 186,
	'Hana Macchia': 158,
	'Han Chiho': 178,
	'Harusaki Air': 180,
	'Hassaku Yuzu': 155,
	'Hayama Marin': 158,
	'Hayase Sou': 170,
	'Ha Yun': 178,
	'Hibachi Mana': 170,
	'Higuchi Kaede': 167,
    'Honma Hiwakari': 153,
	'Hoshikawa Sara': 155,
	'Hoshirube Sho': 177,
	'Hyakumantenbara Salome': 163,
	'Hyona Elatiora': 165,
	'Ibrahim': 177,
	'Ienaga Mugi': 154,
	'Igarashi Rika': 152,
	'Inami Rai': 169,
	'Inui Toko': 162,
	'Ishigami Nozomi': 157,
	'Izumo Kasumi': 158,
	'Joe Rikiichi': 185,
	'Kaburaki Roco': 165,
	'Kagami Hayato': 182,
	'Kaida Haru': 183,
	'Kanae': 175,
	'Kanda Shoichi': 175,
	'Kataribe Tsumugu': 165,
	'Kenmochi Toya': 172,
	'Kingyozaka Meiro': 145,
	'Kitakoji Hisui': 153,
	'Koshimizu Toru': 159,
	'Koyanagi Rou': 173,
	'Kudo Chitose': 159,
	'Kuramochi Meruto': 154,
	'Kurusu Natsume': 171,
	'Kuzuha': 178,
	'Lain Paterson': 163,
	'Lauren Iroas': 176,
	'Layla Alstroemeria': 152,
	'Lee Roha': 165,
	'Leos Vincent': 180,
	'Levi Elipha': 165,
	'Lize Helesta': 158,
	'Luis Cammy': 168,
	'Maimoto Keisuke': 178,
	'Makaino Ririmu': 138,
	'Mashiro Meme': 162,
	'Matsukai Mao': 142,
	'Mayuzumi Kai': 178,
	'Melissa Kinrenka': 161,
	'Mika Melatika': 155,
	'Milan Kestrel': 178,
	'Min Suha': 180,
	'Miyu Ottavia': 155,
	'Moira': 165,
	'Mononobe Alice': 128,
	'Morinaka Kazaki': 135,
	'Murakumo Kagetsu': 169,
	'Nagao Kei': 177,
	'Nagisa Arcinia': 134,
	'Nakao Azuma': 154,
	'Naraka': 144,
	'Nara Haramaung': 173,
	'Naruse Naru': 168,
	'Na Sera': 155,
	'Nishizono Chigusa': 157,
	'Nui Sociere': 165,
	'Oh Jiyu': 171,
	'Oliver Evans': 190,
	'Onomachi Haruka': 154,
	'Otogibara Era': 155,
	'Ponto Nei': 155,
	'Rai Galilei': 158,
	'Ratna Petit': 156,
	'Reza Avanluna': 175,
	'Riksa Dhirendra': 178,
	'Ryushen': 164,
	'Ryu Hari': 157,
	'Saegusa Akina': 168,
	'Saiki Ittetsu': 174,
	'Sakura Ritsuki': 165,
	'Sasaki Saku': 148,
	'Seffyna': 168,
	'Seraph Dazzlegarden': 186,
	'Seto Miyako': 158,
	'Shellin Burgundy': 183,
	'Shibuya Hajime': 180,
	'Shikinagi Akira': 174,
	'Shioriha Ruri': 160,
	'Shirayuki Tomoe': 178,
	'Shishido Akari': 149,
	'Shizuka Rin': 158,
	'Siska Leontyne': 170,
	'Sister Claire': 150,
	'Song Mia': 159,
	'Sophia Valentine': 153,
	'Sorahoshi Kirame': 148,
	'So Nagi': 160,
	'Sukoya Kana': 167,
	'Suo Sango': 148,
	'Suzuhara Lulu': 162,
	'Suzuka Utako': 159,
	'Suzuki Masaru': 153,
	'Suzuya Aki': 155,
	'Tachitsute Toto': 154,
	'Takamiya Rion': 158,
	'Taka Radjiman': 175,
	'Todoroki Kyoko': 165,
	'Todo Kohaku': 162,
	'Tsukimi Shizuku': 149,
	'Tsukino Mito': 151,
	'Umise Yotsuha': 163,
	'Usami Rito': 181,
	'Ushimi Ichigo': 125,
	'Uzuki Kou': 163,
	'Warabeda Meiji': 147,
	'Watarai Hibari': 183,
	'Xia Ekavira': 169,
	'Yaguruma Rine': 141,
	'Yamagami Karuta': 158,
	'Yamiyono Moruru': 162,
	'Yang Nari': 142,
	'Yashiro Kizuku': 180,
	'Yorumi Rena': 154,
	'Yukishiro Mahiro': 152,
	'Yumeoi Kakeru': 175,
	'Yuuhi Riri': 162,
	'Yuki Chihiro': 138,
	'Yuzuki Roa': 141,
	'ZEA Cornelia': 149,
    'Akari Yumeno': 149,
    'Beni Yakumo': 158,
    'Ema Aizawa': 156,
    'Hinano Tachibana': 154,
    'Kuromu Yano': 150,
    'Lisa Hanabusa': 160,
    'Met Komori': 156,
    'Mimi Tosaki': 148,
    'Nazuna Kaga': 154,
    'Noah Kurumi': 155,
    'Qpi Kaminari': 162,
    'Ramune Shiranami': 153,
    'Ren Kisaragi': 165,
    'Runa Shinomiya': 147,
    'Sena Asumi': 155,
    'Sumire Kaga': 154,
    'Toto Kagara': 148,
    'Tsuna Nekota': 157,
    'Uruha Ichinose': 158,
}
base_ref_cm = 173 # kaela
base_ref_h = 1267 # ref version height in px
# base_ref_h / base_ref_cm * 215 (to fit all chart lines with equal spacing)
fixed_heigth_px = 1575

def main():
    for file in os.listdir(os.path.join(file_dir, 'raw')):
        if '.png' in file:
            filename_list = file.replace('.', '_').split('_')
            name_key = ' '.join(filename_list[:-1])
            print(name_key)
            # open images
            img = Image.open(os.path.join(file_dir, 'raw', file))
            ref_img = Image.open(os.path.join(file_dir, 'ref', file))
            target_w, target_h = img.size
            ref_w, ref_h = ref_img.size
            # calculate scaled heights
            target_ref_cm = data[name_key]
            adjusted_h = target_ref_cm / base_ref_cm * base_ref_h
            target_h_2 = round(adjusted_h + adjusted_h / ref_h * (target_h - ref_h))
            # resize image
            aspect_ratio = target_w / target_h
            width = int(target_h_2 * aspect_ratio)
            resized_img = img.resize((width, target_h_2))
            # add padding top
            width, height = resized_img.size
            fixed_heigth = fixed_heigth_px - height
            padded_img = Image.new("RGBA", (width, height + fixed_heigth), (0, 0, 0, 0))
            padded_img.paste(resized_img, (0, fixed_heigth))
            # save
            padded_img.save(os.path.join(file_dir, 'out', file))

if __name__ == '__main__':
    main()
