from modinv import modinv
from modexp import modexp
from Crypto.Util.number import long_to_bytes

q = 117477667918738952579183719876352811442282667176975299658506388983916794266542270944999203435163206062215810775822922421123910464455461286519153688505926472313006014806485076205663018026742480181999336912300022514436004673587192018846621666145334296696433207116469994110066128730623149834083870252895489152123
g = 104831378861792918406603185872102963672377675787070244288476520132867186367073243128721932355048896327567834691503031058630891431160772435946803430038048387919820523845278192892527138537973452950296897433212693740878617106403233353998322359462259883977147097970627584785653515124418036488904398507208057206926

def getPk(line):
  return int(line[12:-2], 16)

def getC1C2(line):
  arr = line.split(',')
  c1 = int(arr[0][4:], 16)
  c2 = int(arr[1][4:-2], 16)
  return (c1, c2)

def readFromFile(filename):
  fp = open(filename, 'r')
  lines = fp.readlines()
  size = len(lines)
  a = []

  for i, line in enumerate(lines):
    if(i%2 == 0):
      pk = getPk(line)
    else:
      (c1,c2) = getC1C2(line)
      a.append((pk, c1, c2))

  fp.close()
  return a

def isQuaRes(c, p):
  return 1 == modexp(c, (p-1)//2, p)

def getBit(args):
  (pk, c1, c2) = args
  return int(isQuaRes(c2, q))

a = readFromFile("output.txt")

bitarray = "".join([str(getBit(i)) for i in reversed(a)])

num = int(bitarray,2)

b = long_to_bytes(num)
print(b)
