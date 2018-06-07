import config as cfg
import fetch


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
            print(x['Name'])
            obj = {}
            obj['Name'] = x['Name']
            obj['seats'] = x['Leading'] + x['Elected']
            obj['clr'] = clr_list[obj['Name']]
            parties.append(obj)
    db['parties'] = parties
    # print(data['Election']['Riding'])
    # extract ridings of interest info
    ridings_list = ["Hamilton Centre", "Hamilton Eastâ\x80\x94Stoney Creek", "Hamilton Mountain", "Hamilton Westâ\x80\x94Ancasterâ\x80\x94Dundas", "Flamboroughâ\x80\x94Glanbrook"]
    ridings_cp = [x for x in data['Election']['Riding'] if x['RNE'] in ridings_list]
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
    return db


print(get_api())
