# つかいかた： じょし フォルダで  python _src/build.py
import io
D=r'C:\Users\taka\OneDrive\デスクトップ\開発・アプリ開発'
s=io.open('_src/src.html',encoding='utf-8').read()
fx=io.open('_src/fx.js',encoding='utf-8').read()
na=io.open(D+r'\なかまわけ\index.html',encoding='utf-8').read()
i=na.index('function jaSay'); j=na.index('\n}\n',i)+3
jasay=na[i:j]
s=s.replace('/*__FX__*/',fx.rstrip()+'\n').replace('/*__JASAY__*/',jasay).replace('/*__DATA__*/',io.open('_src/data.js',encoding='utf-8').read()).replace('/*__PRINTCSS__*/',io.open('_src/printcss.css',encoding='utf-8').read().strip())
io.open('index.html','w',encoding='utf-8',newline='\n').write(s)
print('built',len(s))
