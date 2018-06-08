import config as cfg
import fetch
import io
import json

db = {
    "parties": [
        {"Name": "GRN", "clr": "green", "seats": 0},
        {"Name": "LIB", "clr": "red", "seats": 0},
        {"Name": "NDP", "clr": "orange", "seats": 0},
        {"Name": "PC", "clr": "blue", "seats": 0},
    ],
    "leaders": {
        "ford": "",
        "horwath": "",
        "schreiner": "",
        "wynne": "",
    },
    "ridings": [
        {
            "name": "Burlington",
            "candidates": [
                {
                    "name": "Nadine Bentham",
                    "party": "NAP",
                    "votes": 0
                },
                {
                    "name": "Andrew Drummond",
                    "party": "NDP",
                    "votes": 0
                },
                {
                    "name": "Vince Fiorito",
                    "party": "GRN",
                    "votes": 0
                },
                {
                    "name": "Jim Gilchrist",
                    "party": "LTN",
                    "votes": 0
                },
                {
                    "name": "Jane McKenna",
                    "party": "PC",
                    "votes": 0
                },
                {
                    "name": "Eleanor McMahon",
                    "party": "LIB",
                    "votes": 0
                },
                {
                    "name": "Peter Rusin",
                    "party": "CNS",
                    "votes": 0
                }
            ]
        },
        {
            "name": "Flamborough&ndash;Glanbrook",
            "candidates": [
                {
                    "name": "Janet Errygers",
                    "party": "GRN",
                    "votes": 0
                },
                {
                    "name": "Glenn Langton",
                    "party": "LTN",
                    "votes": 0
                },
                {
                    "name": "Melissa McGlashan",
                    "party": "NDP",
                    "votes": 0
                },
                {
                    "name": "Rudy Miller",
                    "party": "NAP",
                    "votes": 0
                },
                {
                    "name": "Judi Partridge",
                    "party": "LIB",
                    "votes": 0
                },
                {
                    "name": "Roman Sarachman",
                    "party": "TPO",
                    "votes": 0
                },
                {
                    "name": "Donna Skelly",
                    "party": "PC",
                    "votes": 0
                }
            ]
        },
        {
            "name": "Haldimand&ndash;Norfolk",
            "candidates": [
                {
                    "name": "Toby Barrett",
                    "party": "PC",
                    "votes": 0
                },
                {
                    "name": "Danielle Du Sablon",
                    "party": "NDP",
                    "votes": 0
                },
                {
                    "name": "Anne Faulkner",
                    "party": "GRN",
                    "votes": 0
                },
                {
                    "name": "Wasyl Ivan Luczkiw",
                    "party": "MCP",
                    "votes": 0
                },
                {
                    "name": "Dan Matten",
                    "party": "LIB",
                    "votes": 0
                },
                {
                    "name": "Dan Preston",
                    "party": "NAP",
                    "votes": 0
                },
                {
                    "name": "Carolyn Ritchie",
                    "party": "PPO",
                    "votes": 0
                },
                {
                    "name": "Thecla Ross",
                    "party": "FP",
                    "votes": 0
                },
                {
                    "name": "Christopher Rosser",
                    "party": "LTN",
                    "votes": 0
                }
            ]
        },
        {
            "name": "Hamilton Centre",
            "candidates": [
                {
                    "name": "Maria Anastasiou",
                    "party": "IND",
                    "votes": 0
                },
                {
                    "name": "Mary Ellen Campbell",
                    "party": "COM",
                    "votes": 0
                },
                {
                    "name": "Dionne Duncan",
                    "party": "PC",
                    "votes": 0
                },
                {
                    "name": "Andrea Horwath",
                    "party": "NDP",
                    "votes": 0
                },
                {
                    "name": "Tony Lemma",
                    "party": "NAP",
                    "votes": 0
                },
                {
                    "name": "Jason Lopez",
                    "party": "GRN",
                    "votes": 0
                },
                {
                    "name": "Deirdre Pike",
                    "party": "LIB",
                    "votes": 0
                },
                {
                    "name": "Robert Young",
                    "party": "LTN",
                    "votes": 0
                }
            ],
        },
    ],
}


def get_api():
    db = {}
    data = fetch.fetch_data(cfg.config['api'])
    # extract parties info
    parties_cp = data['Election']['Leading']['Party']
    parties = []
    party_list = ["LIB", "PC", "NDP", "GRN"]
    clr_list = {"LIB": "red", "PC": "blue", "NDP": "orange", "GRN": "green"}
    for x in parties_cp:
        if x['Name'] in party_list:
            obj = {}
            obj['Name'] = x['Name']
            obj['seats'] = x['Leading'] + x['Elected']
            obj['clr'] = clr_list[obj['Name']]
            parties.append(obj)
    db['parties'] = parties
    # print(data['Election']['Riding'])
    # extract ridings of interest info
    ridings_list = ["Hamilton Centre", "Hamilton Eastâ\x80\x94Stoney Creek", "Hamilton Mountain",
                    "Hamilton Westâ\x80\x94Ancasterâ\x80\x94Dundas", "Flamboroughâ\x80\x94Glanbrook", "Burlington", "Niagara West", "Haldimandâ\x80\x94Norfolk", "Oakville Northâ\x80\x94Burlington", "Brantfordâ\x80\x94Brant"]
    ridings_cp = [x for x in data['Election']
                  ['Riding'] if x['RNE'] in ridings_list]
    ridings = []
    for x in ridings_cp:
        obj = {}
        obj['name'] = x['RNE'].replace("â\x80\x94", "&ndash;")
        obj['candidates'] = []
        for y in x['Candidate']:
            obj2 = {}
            obj2['name'] = y['FN'] + ' ' + y['LN']
            obj2['party'] = y['PE']
            obj2['votes'] = y['V']
            obj['candidates'].append(obj2)
        ridings.append(obj)
    db['ridings'] = ridings
    db['leaders'] = {"ford": "Won riding", "horwath": "Won riding", "schreiner": "Won riding", "wynne": "Won riding"}
    with io.open("cp.db", "w+", encoding='utf8') as file:
        file.write(json.dumps(db, ensure_ascii=False))
    return db
