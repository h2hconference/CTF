code = open('morse.ino', 'w')

plain_text = "HC-PEY163LCV145-0DE1"

mcd = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

mc = ""
for c in plain_text:
    mc = mc + mcd[c] + ""

print(mc)

# Static content
code.write("//Based on the ATTiny13 blink demo\n\n")
code.write("#include <avr/io.h>\n")
code.write("#include <util/delay.h>\n")



code.write("int main(void)\n{\n")
#Define pin as output
code.write("DDRB |= 0x04;\n")
code.write("uint8_t ds = 500;\n")

code.write("while(1)\n{\n")

code.write("_delay_ms(2000);\n")
for c in mc:
    if c == '.':
        code.write("Short();\n")
    elif c == '-':
        code.write("Long();\n")
    elif c == ' ':
        code.write("_delay_ms(ds);\n")

code.write("\n}\nreturn 0;\n}\n")

code.write("void Short(void)\n{\n")
code.write("PORTB |= 0x04;\n")
code.write("_delay_ms(500);\n")
code.write("PORTB &= ~0x04;\n")
code.write("_delay_ms(250);\n")
code.write("}\n")

code.write("void Long(void)\n{\n")
code.write("PORTB |= 0x04;\n")
code.write("_delay_ms(1000);\n")
code.write("PORTB &= ~0x04;\n")
code.write("_delay_ms(250);\n")
code.write("}\n")

code.close()
