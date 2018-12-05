a=list("dabAcCaCBAcCcaDA")
def main():
  dirtyLoop = False
  for n in range(len(a)-1):
    if abs(ord(a[n])-ord(a[n+1]))==32:
      dirtyLoop = True
      del a[n]
      del a[n]
      break
  if dirtyLoop and len(a)>1:
    main()
  return len(a)
print(main())
