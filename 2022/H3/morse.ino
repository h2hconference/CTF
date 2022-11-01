//Based on the ATTiny13 blink demo

#include <avr/io.h>
#include <util/delay.h>
int main(void)
{
DDRB |= 0x04;
uint8_t ds = 500;
while(1)
{
_delay_ms(2000);
Short();
Short();
Short();
Short();
Long();
Short();
Long();
Short();
Long();
Short();
Short();
Short();
Short();
Long();
Short();
Long();
Long();
Short();
Short();
Long();
Short();
Long();
Long();
Short();
Long();
Long();
Long();
Long();
Long();
Short();
Short();
Short();
Short();
Short();
Short();
Short();
Long();
Long();
Short();
Long();
Short();
Short();
Long();
Short();
Long();
Short();
Short();
Short();
Short();
Long();
Short();
Long();
Long();
Long();
Long();
Short();
Short();
Short();
Short();
Long();
Short();
Short();
Short();
Short();
Short();
Long();
Short();
Short();
Short();
Short();
Long();
Long();
Long();
Long();
Long();
Long();
Long();
Short();
Short();
Short();
Short();
Long();
Long();
Long();
Long();

}
return 0;
}
void Short(void)
{
PORTB |= 0x04;
_delay_ms(500);
PORTB &= ~0x04;
_delay_ms(250);
}
void Long(void)
{
PORTB |= 0x04;
_delay_ms(1000);
PORTB &= ~0x04;
_delay_ms(250);
}
