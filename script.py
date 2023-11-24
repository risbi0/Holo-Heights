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
    'Gavis Bettel': 173,
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
    'Regis Altare': 179,
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
}
base_ref_cm = 173 # kaela
base_ref_h = 1267 # ref version height in px
# trial and error to make height chart in website match with the heights
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
