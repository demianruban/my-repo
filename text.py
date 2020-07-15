# This is planned to be an engine-module for PRG text-based game

#_-_-_-_-_-_-Hero-_-_-_-_-_-_
#
# Char length standard -- 28 chars.

# Planning to add expanding Text Blocks feature.
# Size of Text Blocks will depend on size of terminal.
# Because of prototyping game structure at this moment
# it will be easier to write Designes with ".format" method.


# Text designes down below.

# In common designes located like this:
#
# |-----------____-----------| Wrapper
# |~~~~~~~~~~|HERO|~~~~~~~~~~| Title
# | Hello there, I'm a dork. | Label
# |    * Strength: 12        | Property (item, ability)
# |__________________________| End



# Code down below.

class Text:

    LINE_LENGTH = 28

    designes = {
    
        'Wrapper': ('_-{}-_',
                    '|-{}-|',
                    '--{}--'),

        'Title' : ('|~|{}|~|',
                    '-*{}*-'),
        
        'Property' : '| {}* {}: {} |',
        
        'End' : '|_{}_|'
    }
    
    def wrap_text(self, text):
        
        text = "Hello my name is Demian. I'm here to tell you shit."
            
        vowels = ['a', 'e', 'i', 'o', 'u']

        calc = len(text) / (Text.LINE_LENGTH - 4)

        print(calc)
    
    def make_line(self, string: str, inner_text: str) -> str:
        '''Checks if char need to be repeated or not.
        Repeats the chars to make beautiful bars.
        Works good with even numbers NOT odd.
        '''

        def cycle(num1, num2):
            while True:
                yield num1
                yield num2
        
        # get rid of difference between patterns.
        
        for i in range(len(string)):
            if string[i] == '{':
                Lpttrn = string[0:i]
                Rpttrn = Lpttrn[-1::-1] # reversed
                
        calc = (Text.LINE_LENGTH - len(inner_text)) / 2

        leftside   = Lpttrn * int((calc / len(Lpttrn)))
        rightside  = Rpttrn * int((calc / len(Rpttrn)))

        output = leftside + inner_text + rightside
            
        if len(output) < 28: # just adding chars to the leftside
            print(output, len(output))

            side_iterator   = cycle(0, 1)
            lpttrn_iterator = cycle(0, 1)
            rpttrn_iterator = cycle(0, 1)
            
            while len(output) <= 28:
                
                if next(side_iterator):
                    
                    leftside = Lpttrn[next(lpttrn_iterator)] + leftside
                    
                else:
                    rightside = rightside + Rpttrn[next(rpttrn_iterator)]
                    
                output = leftside + inner_text + rightside
                
##        elif len(output) > 28: # just remove chars from the leftside
##            diff = len(output)-28
##            leftside = leftside[0:length-diff]

        return leftside + inner_text + rightside
    
    def text_block(self):
        pass
    
name = 'Demian'
compare = "-_-_-_-_-_-Demian-_-_-_-_-_-"
content = "Hello my name is Demian. I'm here to tell you shit."

one = Text()

print(one.make_line(Text.designes['Wrapper'][0], 'Demian'))

print(compare, len(compare))
