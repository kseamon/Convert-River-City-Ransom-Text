"""
Copyright (c) 2013, Karl Seamon
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from optparse import OptionParser
import sys

hex2char = {
  'F4': '0',
  'F5': '1',
  'F6': '2',
  'F7': '3',
  'F8': '4',
  'F9': '5',
  'FA': '6',
  'FB': '7',
  'FC': '8',
  'FD': '9',
  'C0': 'A',
  'C1': 'B',
  'C2': 'C',
  'C3': 'D',
  'C4': 'E',
  'C5': 'F',
  'C6': 'G',
  'C7': 'H',
  'C8': 'I',
  'C9': 'J',
  'CA': 'K',
  'CB': 'L',
  'CC': 'M',
  'CD': 'N',
  'CE': 'O',
  'CF': 'P',
  'D0': 'Q',
  'D1': 'R',
  'D2': 'S',
  'D3': 'T',
  'D4': 'U',
  'D5': 'V',
  'D6': 'W',
  'D7': 'X',
  'D8': 'Y',
  'D9': 'Z',
  'DA': 'a',
  'DB': 'b',
  'DC': 'c',
  'DD': 'd',
  'DE': 'e',
  'DF': 'f',
  'E0': 'g',
  'E1': 'h',
  'E2': 'i',
  'E3': 'j',
  'E4': 'k',
  'E5': 'l',
  'E6': 'm',
  'E7': 'n',
  'E8': 'o',
  'E9': 'p',
  'EA': 'q',
  'EB': 'r',
  'EC': 's',
  'ED': 't',
  'EE': 'u',
  'EF': 'v',
  'F0': 'w',
  'F1': 'x',
  'F2': 'y',
  'F3': 'z',
  'BA': ',',
  'B2': '!',
  '2A': '\'',
  'B9': '&',
  'B6': '.',
  'B1': '"',
  'B3': '?',
  'B4': '-',
  'B7': ':',
  'FE': '$',
  'B5': '%',
  '00': ' ',
  'B0': '*',
}

end_hex2char = {
  '90': 'A',
  '91': 'B',
  '92': 'C',
  '93': 'D',
  '94': 'E',
  '95': 'F',
  '96': 'G',
  '97': 'H',
  '98': 'I',
  '99': 'J',
  '9A': 'K',
  '9B': 'L',
  '9C': 'M',
  '9D': 'N',
  '9E': 'O',
  '9F': 'P',
  'A0': 'Q',
  'A1': 'R',
  'A2': 'S',
  'A3': 'T',
  'A4': 'U',
  'A5': 'V',
  'A6': 'W',
  'A7': 'X',
  'A8': 'Y',
  'A9': 'Z',
  'AF': '.',
}

def convert_lookup(lookup):
  return dict([(lookup[k], k) for k in lookup.keys()])

char2hex = convert_lookup(hex2char)
end_char2hex = convert_lookup(end_hex2char)

def hexchars(input):
  input = input.replace(' ', '').upper()
  for i in xrange(0, len(input), 2):
    yield ''.join(input[i:i+2])

def translate(input, lookup):
  return ''.join([lookup[c] for c in input])

def main(argv):
  parser = OptionParser();
  parser.add_option('-t', '--text', dest='text',
      help='Text to convert to Hex')
  parser.add_option('-T', '--endtext', dest='endtext',
      help='Text to convert to end credit Hex')
  parser.add_option('-x', '--hex', dest='hex',
      help='Hex to convert to Text')
  parser.add_option('-X', '--endhex', dest='endhex',
      help='credit Hex to convert to Text')

  (options, args) = parser.parse_args()

  if options.hex:
    print translate(hexchars(options.hex), hex2char)
  elif options.endhex:
    print translate(hexchars(options.endhex), end_hex2char)
  elif options.text:
    print translate(options.text, char2hex)
  elif options.endtext:
    print translate(options.endtext.upper(), end_char2hex)

  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv))
