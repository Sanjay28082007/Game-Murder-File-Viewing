from morse3 import Morse
import json
from deep_translator import GoogleTranslator
import csv

# --------------------- file save details
# files_read = set()
# suspects_asked = set()
# decoded_clues = {}
# current_stage = "1"
# timestamp = date.strftime("%Y-%m-%d")
#
# save_dict = {
#     "files_read": files_read,
#     "suspects_asked": suspects_asked,
#     "decoded_clues": decoded_clues,
#     "current_stage": current_stage,
#     "timestamp": timestamp
# }


data = {chr(code): Morse(chr(code)).stringToMorse() for code in range(33, 123) if
        Morse(chr(code)).stringToMorse() != KeyError}


def help_morse():
    with open("Admin_files/help/morse.json", 'w', encoding='utf-8') as f:
        json.dump(data, f)


get_language = GoogleTranslator.get_supported_languages(GoogleTranslator(), as_dict=True)

# sample_text_list = []
# for keys in get_language:
#     sample_text = GoogleTranslator(source="en", target=keys).translate("sample")
#     sample_text_list.append(sample_text)

# Here is the list below
sample_text_list = [
    "monster", "mostër", "ናሙና", "عينة", "նմուշ", "নমুনা", "muestra", "nümunə", "misali", "lagin",
    "узор", "নমুনা", "नमूना", "uzorak", "проба", "mostra", "sample", "chitsanzo", "样本", "樣本",
    "campione", "uzorak", "vzorek", "prøve", "ނަމޫނާ", "नमूना", "monster", "sample", "specimeno",
    "proov", "kpɔɖeŋu", "sample", "näyte", "échantillon", "foarbyld", "mostra", "ნიმუში", "Probe",
    "δείγμα", "techapyrã", "નમૂનો", "echantiyon", "samfur", "laʻana", "דוגמה", "नमूना", "qauv",
    "minta", "sýni", "nlele", "pagarigan", "sampel", "sampla", "campione", "サンプル", "conto",
    "ಮಾದರಿ", "үлгі", "គំរូ", "ingero", "नमुनो", "샘플", "sampul", "nimûne", "نموونە", "үлгү",
    "ຕົວຢ່າງ", "exemplar", "paraugs", "ndakisa", "pavyzdys", "ekyokulabirako", "Probe", "примерок",
    "नमूना", "santionany", "sampel", "സാമ്പിൾ", "kampjun", "tauira", "नमुना", "নমুনা", "entirna",
    "жишээ", "နမူနာ", "नमूना", "prøve", "ନମୁନା", "fakkeenya", "نمونه", "نمونه", "próbka", "amostra",
    "ਨਮੂਨਾ", "rikch'ana", "eșantion", "образец", "fa'ata'ita'iga", "नमूना", "sampall", "sekao",
    "узорак", "mohlala", "muenzaniso", "نمونو", "නියැදිය", "vzorka", "vzorec", "tusaale", "muestra",
    "conto", "mfano", "prov", "намуна", "மாதிரி", "үрнәк", "నమూనా", "ตัวอย่าง", "ኣብነት", "xikombiso",
    "örnek", "nusga", "nhwɛso", "зразок", "نمونہ", "ئەۋرىشكە", "namuna", "mẫu", "sampl", "isampulu",
    "מוסטער", "apẹẹrẹ", "isampula"
]

languages = []
index = 0
for language, code in sorted(get_language.items()):
    new_dict = {
        "code": code,
        "language": language,
        "sample text": sample_text_list[index]
    }
    languages.append(new_dict)
    index += 1


names_list = ['code', 'language', "sample text"]

with open("Admin_files/help/language.csv", 'w', encoding='utf-8', newline='') as output_file:
    languages_dialect = csv.excel
    languages_dialect.delimiter = ','
    languages_dialect.quoting = csv.QUOTE_NONNUMERIC

    headings_writer = csv.writer(output_file, dialect=languages_dialect)
    headings_writer.writerow(names_list)
    writer = csv.DictWriter(output_file, dialect=languages_dialect, fieldnames=names_list)
    writer.writerows(languages)



def suspect_master():
    with open("Files/suspects.json", 'r+', encoding='utf-8') as file:
        file_data = json.load(file)
        file.seek(0)
        file.truncate()
        new_list = []
        for inner_data in file_data:
            for description, name in inner_data.items():
                name_dict = {name.casefold(): inner_data}
                new_list.append(name_dict)
                break

        json.dump(new_list, file, indent=2)


suspect_master()
