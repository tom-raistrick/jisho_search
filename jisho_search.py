import requests

result_count = 0
language = 'English'


def search_function(sf_language, sf_search_input):
    if sf_language == 'English':
        search_url = 'https://jisho.org/api/v1/search/words?keyword=%22' + sf_search_input + '%22'
    else:
        search_url = 'https://jisho.org/api/v1/search/words?keyword=' + sf_search_input
    sf_search_json = requests.get(url=search_url)
    sf_result_limit = len(sf_search_json.json()['data'])
    return sf_search_json, sf_result_limit


def result_function(rf_result_count, rf_result_limit, rf_language, rf_search_input):
    print('\nSearch term: ' + rf_search_input)
    print('Result ' + str(rf_result_count + 1) + ' of ' + str(rf_result_limit) + '.')
    print('\nJapanese Translation: ' + search_json.json()['data'][rf_result_count]['slug'])
    print('Japanese Reading: ' + search_json.json()['data'][rf_result_count]['japanese'][0]['reading'])
    print('English Translation: ' + search_json.json()['data'][rf_result_count]['senses'][0]['english_definitions'][0] + '\n')
    if rf_result_count == rf_result_limit - 1:
        print("No more results.  Returning to search.")
        return
    elif rf_result_count < rf_result_limit - 1:
        menu_char = input("Enter 'n' to view next result, or 's' to return to search: ")
        if menu_char == 'n':
            rf_result_count += 1
            result_function(rf_result_count, rf_result_limit, rf_language, rf_search_input)
        elif menu_char == 's':
            return


def language_function(lf_search_input):
    if lf_search_input == '-e':
        lf_language = 'English'
        return lf_language
    elif lf_search_input == '-j':
        lf_language = 'Japanese'
        return lf_language


while True:
    print("\nTyped language is set to " + language + ".\n")
    search_input = input("Enter search term: ")
    if search_input == '-e' or search_input == '-j':
        language = language_function(search_input)
    else:
        search_json, result_limit = search_function(language, search_input)
        if not search_json.json()['data']:
            print('Nothing found.  Please try again.')
        else:
            result_function(result_count, result_limit, language, search_input)
