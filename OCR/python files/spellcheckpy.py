import pkg_resources
from symspellpy import SymSpell, Verbosity

def insert_spaces(filename):
    '''Insert spaces before and after special characters in each line'''
    with open(filename,'r') as file:
        lines=file.readlines()
        for line in lines:
            index=lines.index(line)
            for c in line[:]:
                if not c.isalnum():
                    line = line.replace(c,  " %s " % c)
                    lines[index]=line
            
    return lines

def string_to_list(list_of_strings):
    '''Convert the list of lines to a list of lists of words'''
    spaced_line=[]
    for line in list_of_strings:
        spaced_line.append(line.split())
    return spaced_line
    
def read_file(filename):
    '''Read the words and charactrs in the input file.
    
    Output: list of lists
    
    Example: a file containing "Hello, World.\n Good Morning." gives
             output [['Hello', ',', 'World', '.'],['Good', 'Morning', '.']]
    '''
    lines_with_spaces=insert_spaces(filename)
    words_n_chars=string_to_list(lines_with_spaces)
    return words_n_chars

def write_file(filename, words):
    '''Write in a file.
    ----------------
    Input Parameters
    ----------------
    filename: string, mandatory
        Filename of the file to be generated 
    words: list of lists, mandatory
        a list of lists of words.
    ----------------
    Example: if L=[['Hello', ',', 'World', '.'],['Good', 'Morning', '.']]
             then calling write_file('a.txt',L) generate a file named 'a.txt' 
             with content "Hello , World .\n Good Morning ."
    '''
    with open(filename, "w") as file:
        file.writelines(' '.join(str(j) for j in i) + '\n' for i in words)
    print(filename + " -> generated.")


class SpellCheck():
    '''Spelling check using symspellpy library.
    ----------------
    Input Parameters
    ----------------
    filename: string, mandatory
        Filename of the text file which is to be checked. 
        Whole path needs to be entered if the text file is 
        in a different directory w.r.t this program file.
        *** Assumed to be a file with .txt extension
    max_edit_dist : int, optional, default_value=2
        Maximum distance allowed between the word and the corrected word.
        *** max_edit_dist >= 0
    length_of_prefix : int, optional, default_value=7
        The length of word prefixes used for spell checking.
        *** length_of_prefix >= 1 and length_of_prefix > max_edit_dist
    '''
    def __init__(self, filename, max_edit_dist=2, length_of_prefix=7):
        self.txtfile = read_file(filename)
        self.new_name = filename[0:-4]+"_corrected.txt"
        self.maxd = max_edit_dist
        self.prefix_len = length_of_prefix
    
    def replace(self):
        ''' Generates a new text file by correcting the spellings'''
        sym_spell = SymSpell(max_dictionary_edit_distance=self.maxd, 
                             prefix_length=self.prefix_len)
        dictionary_path = pkg_resources.resource_filename("symspellpy", 
                                        "frequency_dictionary_en_82_765.txt")
        # term_index is the column of the term and count_index is the
        # column of the term frequency
        sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
        
        txtfile_corrected=self.txtfile
        for line in txtfile_corrected:
            for word in line:
                if (word.isalpha() and len(word)>1) :
                    input_term = word
                    suggestions = sym_spell.lookup(input_term, Verbosity.TOP, 
                                                   max_edit_distance=self.maxd,
                                                   transfer_casing=True, 
                                                   include_unknown=True)
                    line[line.index(word)]=suggestions[0].term
        write_file(self.new_name, txtfile_corrected)
        

    