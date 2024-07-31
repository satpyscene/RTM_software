      PROGRAM DECOM_PF

! MODIFICATIONS:
!    15 JUN, 2005 - Had to modify how this program reads in the phase 
!                   function files in order to properly read my files
!                   (Chris Yost)
!    15 JUN, 2005 - Changed the length of strings fn and out from
!                   20 to 58


!    09 Mar, 2011 - Improve code and ....(Chenxi Wang)               

      character*150 fn, out                        ! CY, 15-06-2005
      real pmom(0:300),pfitdm(0:300),pfit(0:300),ftrunc
!     real pl(301),ang(450)
!     real phsmom(450),phsfit(450),phstrc(450)
      real omega, fdelta, ce, gfact
      real out_omega(120), out_ce(120), out_ftrunc(120)
      integer nstr, i, j, numfiles
      integer ihabit,irough,n_wn,n_re

!     CHARACTER*30,DIMENSION(10)::habit_name
!     CHARACTER*30,DIMENSION(3)::rough_name
!     character*150 temp_outputdir, temp_inputdir, filename
      character*150 inDir, outDir, inFile, outFile
      CHARACTER*100 F_NAME
      character*30 F_WL
      character*10 arg1
      DOUBLE PRECISION :: wl
      integer LA1,LA2, band_mode

      logical path_exist

      INTEGER :: RADII(90)
!     DATA RADII/2,4,6,8,10,12,14,16,18,20,
!    & 24,28,32,36,40,44,48,52,56,60/
      integer re
     
!     WRITE(DIR,'(2A)')'./DATABASE/'
!     DIR = './DATABASE/WATER/'
!     inDir = ''
!     write(inDir,'(2A)') TRIM(DIR), 'BULK_PROP/'
!     outDir = ''
!     write(outDir,'(2A)') TRIM(DIR), 'P_EXPANSION/'

      call getarg(1,inDir)
      call getarg(2,outDir)
      call getarg(3,arg1)
      read(arg1, *) band_mode
      call getarg(4,arg1)
      read(arg1, *) nstr
      write(*,*) nstr
!     nstr=32

      open(111, file='./INPUT/input_re.dat',status='unknown')
      read(111, *) n_re
      do i=1,n_re
        read(111, *) RADII(I)
      end do
      close(111)

      if (band_mode == 0) then
        open(112, file='./INPUT/wl.dat',status='unknown')
        read(112, *) n_wn
      elseif (band_mode == 1) then
        open(112,file='./INPUT/input_band.dat',status='unknown')
        read(112, *) n_wn
      endif

      do ihabit = 1, n_wn
        if (band_mode == 0) then
          read(112, *) wl
          WRITE(F_WL,'(F10.2)') wl
  !       WRITE(*,*) F_WL
          DO I=1,30
             LA1=I
             IF(F_WL(I:I) /= " ") EXIT
          END DO
          DO I=30,1,-1
             LA2 = I
             IF(F_WL(I:I) /= " ") EXIT
          END DO
          DO I=LA1,LA2
             IF(F_WL(I:I) == ".") F_WL(I:I)="p"
          ENDDO
        elseif (band_mode == 1) then
          read(112, *) F_WL
        endif

        do irough = 1,n_re
          re = RADII(irough)
!         temp_outputdir = ''
!         write(temp_outputdir,"(A)")  './DATABASE/P_EXPANSION/'
!         temp_inputdir = ''
!         write(temp_inputdir,"(A)")   TRIM(DIR)
!         inquire(FILE=temp_outputdir,exist=path_exist)
!         if (path_exist) then
!           !call system('rm -r '//temp_outputdir)
!           !call system('mkdir '//temp_outputdir)
!         else
!           call system('mkdir '//temp_outputdir)
!         endif

          F_NAME  = ''
          if (band_mode == 0) then
            write(F_NAME,'(3A,I3.3,A)')
     +                      'WVN_',F_WL(LA1:LA2),'_DE_',re,'.dat'
          elseif (band_mode == 1) then
            write(F_NAME,'(2A,I3.3,A)') trim(F_WL),'_DE_',re,'.dat'
          endif

          inFile  = ''
          write(inFile,*) trim(inDir)//trim(F_NAME)
          outFile = ''
          write(outFile,*) trim(outDir)//trim(F_NAME)

          open (9,file=outFile,status='unknown')
          call bfit(inFile,nstr,pmom,pfitdm,pfit,ftrunc,ce,omega,
     +              gfact,fdelta)
          out = 'truncation factor (ft) and f-delta'

          do i=1,4
            write (9,*)
          enddo
          write (9,*) 'Ce, omega0, g-factor, f-delta'
          write (9,"(4(E15.5,2X))") ce,omega,gfact,fdelta
          write (9,*)
          write (9,*) 'truncation = y  1-Jul-2002'
          write (9,"(2(F9.6,1X),A34)") ftrunc,fdelta,out
          write (9,*) nstr, 'coefficients'
          do i = 0, nstr
            write (9,"(I4,F12.7)") i+1,pfit(i)
          enddo
          close(9)

          if (abs(wl - 0.55D0) .LT. 1.0E-03) then
            write(outFile,'(2A,I3.3,A)') trim(outDir),
     +         'WN_REF_RE_',re,'.dat'
            open (9,file=outFile,status='unknown')
            do i=1,4
              write (9,*)
            enddo
            write (9,*) 'Ce, omega0, g-factor, f-delta'
            write (9,"(4(E15.5,2X))") ce,omega,gfact,fdelta
            write (9,*)
            write (9,*) 'truncation = y  1-Jul-2002'
            write (9,"(2(F9.6,1X),A34)") ftrunc,fdelta,out
            write (9,*) nstr, 'coefficients'
            do i = 0, nstr
              write (9,"(I4,F12.7)") i+1,pfit(i)
            enddo
            close(9)
          endif
!         out_ce(irough)=ce
!         out_omega(irough)=omega
!         out_ftrunc(irough)=ftrunc
        enddo
!       WRITE(outFile,'(2A,I5.5,A)') TRIM(outDir),
!    +                              'WVN_',ihabit,'.SeaFog'
!       OPEN(UNIT=111,FILE=TRIM(outFile),STATUS='UNKNOWN')
!       WRITE(111,'(18F10.5)') out_ce(1:18)
!       WRITE(111,'(18F10.5)') out_omega(1:18)
!       WRITE(111,'(18F10.5)') out_ftrunc(1:18)
!       CLOSE(111)

      enddo
      close(112)
!     close(1)
      end

c----------------------------------------------------------------------------
c----------------------------------------------------------------------------
c  bfit(fn,nstr,pmom,pfit,ftrunc,ce,omega,gfact,fdelta):
c
c  This program computes the delta-fit coefficients as well
c  as delta-M moments for DISORT users
c
c!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
c  Important:
c    In order to apply it, use pfit(nstr) as the truncation factor
c    and use (pfit(i)-pfit(nstr))/(1-pfit(nstr)) as the new moments
c    of the phase function, which is similar to the delta-M approach
c!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
c 
c  Input variables: 
c         
c   fn (character*80) :   filename of the phase function 
c         it has to be in such format:
c
c         the first line:  
c         1 integer number -- the number of scattering angles nn (nn < 2000)
c
c         from line 2 to line nn+1: 
c         2 real number -- angle (in degree), phase function   
c         (the phase function has to be normalized to 2: int_-1^1  P dmu = 2. 
c          for example, P = 1 for isotropic phase function)
c
c   nstr (integer) : the number of streams
c
c  Output:
c   
c   pmom    the regular moments which DISORT needs for PMOM
c           (real number starting at dimension0, 
c           1-d vector with length 0:300) 
c                            -------------
c   pfitdm  the fitted "moments" which DISORT needs for PMOM
c           with deltam = .true.
c           (real number starting at dimension0, 
c           1-d vector with length 0:300) 
c                            -------------
c   pfit and ftrunc    in case you do not use disort, this is  
c           the "moments" from the delta-fit after delta-truncation 
c           with truncation factor ftrunc
c           (ftrunc: real)
c           (pfit: real number starting at dimension0, 
c           1-d vector with length 0:300) 
c
c----------------------------------------------------------------------------
c
        subroutine bfit(fn,nstr,pmom,pfitdm,pfit,ftrunc,c,o,g,f)
        character*150 fn 
        character*100 garbage                          ! CY, 15-06-2005
        integer nstr, nn, i, j, k, ii, jj, kk
        real pmom(0:*),pfit(0:*),pfitdm(0:*),ftrunc
        real ang(2000),phs(2000),xmu(2000)
        real x1(200),w1(200),y1(200)
        real x2(800),w2(800),y2(800)
        real x(1000),w(1000),y(1000),xx(1000),angtrun
        real c,o,g,f,veff,seff
        real reff, sigma_sca                  ! CW, 10-03-2011
        real lambda, De, iwc, mmD, sigma_ext            ! CY, 15-06-2005
c       read the phase function file
        open (8,file=fn,status="old")
        read (8,*) reff,veff,seff,c,o,g
        f = 0.0
        nn = 498
        do i=1,nn
          read (8,*) ang(i),phs(i)
        enddo
        close(8)
ccc     ang are in degrees (Theta), not cos(Theta)
        if (abs(ang(nn)).le.1. .and. abs(ang(1)).le.1.) then  
          do i=1,nn
            ang(i)=acos(ang(i))*180./3.1415926
          enddo
        endif
ccc  interpolate the phase function data for future integrations
c
         angtrun=cosd( 5. )
c       
        call gauleg(angtrun,1.,x1,w1,100)
        call gauleg(0.,angtrun,x2,w2,400)
        do i=1,100
          w(i)=w1(101-i)
          x(i)=-x1(101-i)
          w(1001-i)=w1(101-i)
          x(1001-i)=x1(101-i)
        enddo
        do i=1,400
          w(i+100)=w2(i)
          x(i+100)=-x2(401-i)
          w(901-i)=w2(i)
          x(901-i)=x2(401-i)
        enddo
        do i=1,1000
          xx(i)=acos(x(i))*180./3.1415926
        enddo
c
        call myspline(nn,ang,phs,1000,xx,y)
ccc  in case you want to compare interpolated phs with the true phs
c       print *,  ' 1000 '
c       do i=1,1000
c       print '(2e15.8)', acos(x(i))*180./3.1415926, y(i)
c       enddo
ccc  compute the moments 
        call calmom(x,y,w,nstr,pmom)
ccc  compute pfit 
        call calfit(x,y,nstr,pmom,pfitdm)
        ftrunc=pfitdm(nstr)
        do i=0,nstr
          pfit(i)=(pfitdm(i)-ftrunc)/(1.-ftrunc)
        enddo
        end
c
c
        subroutine calfit(x,y,nstr,pmom,pfitdm)
        integer nstr,ndata,ma, i, j, k, l, nkp
        real x(*),y(*),pmom(0:*),pfitdm(0:*)
        real u(1000,301),b(1000),cor,a(301)
        real pl(301),apl(0:300,1000)
ccc   compute all the legendre polynomials at all quadreatures
        do i=1,1000
        call fleg(x(i),pl,nstr+1) 
          do j=0,nstr
            apl(j,i)=pl(j+1)
          enddo
        enddo
ccc  keep the first a few moments pmom(0:nkp)
        nkp=2
ccc  compute b and u for the fits 
        ndata=1000
        ma=nstr-nkp
        do k=1,1000
         b(k)=1.
         do l=0,nkp
          b(k)=b(k)-(2.*l+1)*pmom(l)*apl(l,k)/y(k)
         enddo
         u(k,ma)=0.
         do i=0,nstr-1
          u(k,ma)=u(k,ma)-(2.*i+1.)*apl(i,k)/y(k)
         enddo
         do l=nkp+1,nstr-1
          u(k,l-nkp)=(2.*l+1.)*apl(l,k)/y(k)
         enddo
        enddo 
ccc  singular value decomposition fitting to derive b
        call svdfit(ndata,a,ma,u,b,cor) 
ccc  the moments which we want to keep
        do i=0,nkp
          pfitdm(i)=pmom(i)
        enddo
ccc  other moments (the delta-truncation needs to be considered)
ccc  the fitted values are the ones after truncation factor
ccc  So, the true moments should add the truncation factor
        pfitdm(nstr)=a(nstr-nkp)
        do i=nkp+1,nstr-1
        pfitdm(i)=a(i-nkp)
        enddo
        end
c
c
        subroutine calmom(x,y,w,nstr,pmom)
        real x(1000),y(1000),w(1000),pmom(0:*)
        integer nstr, i, j, k
        real pl(301),apl(0:300,1000)
ccc   compute all the legendre polynormials at all quadreatures
        do i=1,1000
        call fleg(x(i),pl,nstr+1) 
         do j=0,nstr
          apl(j,i)=pl(j+1)
         enddo
        enddo
ccc   compute the moments
        do j=0,nstr
         pmom(j)=0.
         do i=1,1000
         pmom(j)=pmom(j)+w(i)*y(i)*apl(j,i)*0.5   
         enddo
        enddo   
ccc   if pmom(0) is not 1, (e.g., 0.5, pi, ...) rescale y
        if (abs(pmom(0)-1.) .gt.0.05) then
         do i=1,1000
         y(i)=y(i)/pmom(0)
         enddo
        endif
ccc   scaling: pmom(0) should change from 2 to 1
!       print *, 'pmom(0)=', pmom(0)
        do j=1,nstr
         pmom(j)=pmom(j)/pmom(0)
        enddo
        pmom(0)=1.
        return
        end
c               
c
        subroutine myspline(n,x,y,nn,xn,yn)
c---------spline fit to derive the yy value at point xx
c  Inputs:
c     n:    the length of x and y
c     x(n): the x values which x(1) < x(2) ... < x(n)
c     y(n): the y value which correspondent to x(n)
c     nn:  the length of vector xx and yy
c     xn:  the x value at which y value is wanted
c
c  Outputs:
c     yn: the wanted y value from the fitting
c
c  Internal variables:
c     yp1: the derivative of y over x at x(1), for natural bc, yp1=1.e31
c     ypn: the derivative of y over x at x(n), for natural bc, ypn=1.e31
c     y2(n): the second derivatives
c
      integer n,nn,ny2,i
      parameter (ny2=5000) 
      real x(*),y(*),xn(*),yn(*),y2(ny2),xx,yy,yp1,ypn
c--------the sorting which makes sure x(1)<x(2)<...<x(n)-------
        call sort2(n,x,y) 
c--------start spline------------
        yp1=1.e31
        ypn=1.e31
        call spline(x,y,n,yp1,ypn,y2)
        do i=1,nn
        xx = xn(i)
        call splint(x,y,y2,n,xx,yy)
        yn(i) = yy
        enddo
        return
        end 
        
c
      SUBROUTINE spline(x,y,n,yp1,ypn,y2) 
      INTEGER n,NMAX, ny2
      PARAMETER (NMAX=5000) 
      parameter (ny2=5000) 
      REAL yp1,ypn,x(n),y(n),y2(ny2) 
      INTEGER i,k 
      REAL p,qn,sig,un,u(NMAX) 
      if (yp1.gt..99e30) then 
        y2(1)=0. 
        u(1)=0. 
      else 
        y2(1)=-0.5 
        u(1)=(3./(x(2)-x(1)))*((y(2)-y(1))/(x(2)-x(1))-yp1) 
      endif 
      do 11 i=2,n-1 
        sig=(x(i)-x(i-1))/(x(i+1)-x(i-1)) 
        p=sig*y2(i-1)+2. 
        y2(i)=(sig-1.)/p 
        u(i)=(6.*((y(i+1)-y(i))/(x(i+1)
     $ -x(i))-(y(i)-y(i-1))/(x(i)-x(i-1)))/(x(i+1)-x(i-1))-sig* 
     $ u(i-1))/p 
11    continue 
      if (ypn.gt..99e30) then 
        qn=0. 
        un=0. 
      else 
        qn=0.5 
        un=(3./(x(n)-x(n-1)))*(ypn-(y(n)-y(n-1))/(x(n)-x(n-1))) 
      endif 
      y2(n)=(un-qn*u(n-1))/(qn*y2(n-1)+1.) 
      do 12 k=n-1,1,-1 
        y2(k)=y2(k)*y2(k+1)+u(k) 
12    continue 
      return 
      END 
c
      SUBROUTINE splint(xa,ya,y2a,n,x,y) 
      INTEGER n 
      REAL x,y,xa(n),y2a(n),ya(n) 
      INTEGER k,khi,klo 
      REAL a,b,h 
      klo=1 
      khi=n 
1     if (khi-klo.gt.1) then 
        k=(khi+klo)/2 
        if(xa(k).gt.x)then 
          khi=k 
        else 
          klo=k 
        endif 
      goto 1 
      endif 
      h=xa(khi)-xa(klo) 
      if (h.eq.0.) pause 'bad xa input in splint' 
      a=(xa(khi)-x)/h 
      b=(x-xa(klo))/h 
      y=a*ya(klo)+b*ya(khi)+((a**3-a)*y2a(klo)+
     $   (b**3-b)*y2a(khi))*(h*h)/6. 
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
c
      SUBROUTINE sort2(n,arr,brr) 
      INTEGER n,M,NSTACK 
      REAL arr(n),brr(n) 
      PARAMETER (M=7,NSTACK=50) 
      INTEGER i,ir,j,jstack,k,l,istack(NSTACK) 
      REAL a,b,temp 
      jstack=0 
      l=1 
      ir=n 
1     if(ir-l.lt.M)then 
        do 12 j=l+1,ir 
          a=arr(j) 
          b=brr(j) 
          do 11 i=j-1,1,-1 
            if(arr(i).le.a)goto 2 
            arr(i+1)=arr(i) 
            brr(i+1)=brr(i) 
11        continue 
          i=0 
2         arr(i+1)=a 
          brr(i+1)=b 
12      continue 
        if(jstack.eq.0)return 
        ir=istack(jstack) 
        l=istack(jstack-1) 
        jstack=jstack-2 
      else 
        k=(l+ir)/2 
        temp=arr(k) 
        arr(k)=arr(l+1) 
        arr(l+1)=temp 
        temp=brr(k) 
        brr(k)=brr(l+1) 
        brr(l+1)=temp 
        if(arr(l+1).gt.arr(ir))then 
          temp=arr(l+1) 
          arr(l+1)=arr(ir) 
          arr(ir)=temp 
          temp=brr(l+1) 
          brr(l+1)=brr(ir) 
          brr(ir)=temp 
        endif 
        if(arr(l).gt.arr(ir))then 
          temp=arr(l) 
          arr(l)=arr(ir) 
          arr(ir)=temp 
          temp=brr(l) 
          brr(l)=brr(ir) 
          brr(ir)=temp 
        endif 
        if(arr(l+1).gt.arr(l))then 
          temp=arr(l+1) 
          arr(l+1)=arr(l) 
          arr(l)=temp 
          temp=brr(l+1) 
          brr(l+1)=brr(l) 
          brr(l)=temp 
        endif 
        i=l+1 
        j=ir 
        a=arr(l) 
        b=brr(l) 
3       continue 
          i=i+1 
        if(arr(i).lt.a)goto 3 
4       continue 
          j=j-1 
        if(arr(j).gt.a)goto 4 
        if(j.lt.i)goto 5 
        temp=arr(i) 
        arr(i)=arr(j) 
        arr(j)=temp 
        temp=brr(i) 
        brr(i)=brr(j) 
        brr(j)=temp 
        goto 3 
5       arr(l)=arr(j) 
        arr(j)=a 
        brr(l)=brr(j) 
        brr(j)=b 
        jstack=jstack+2 
        if(jstack.gt.NSTACK)pause 'NSTACK too small in sort2' 
        if(ir-i+1.ge.j-l)then 
          istack(jstack)=ir 
          istack(jstack-1)=i 
          ir=j-1 
        else 
          istack(jstack)=j-1 
          istack(jstack-1)=l 
          l=i 
        endif 
      endif 
      goto 1 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
c
      SUBROUTINE gauleg(x1,x2,x,w,n) 
      INTEGER n 
      REAL x1,x2,x(n),w(n) 
      DOUBLE PRECISION EPS 
      PARAMETER (EPS=3.d-14) 
      INTEGER i,j,m 
      DOUBLE PRECISION p1,p2,p3,pp,xl,xm,z,z1 
      m=(n+1)/2 
      xm=0.5d0*(x2+x1) 
      xl=0.5d0*(x2-x1) 
      do 12 i=1,m 
        z=cos(3.141592654d0*(i-.25d0)/(n+.5d0)) 
1       continue 
          p1=1.d0 
          p2=0.d0 
          do 11 j=1,n 
            p3=p2 
            p2=p1 
            p1=((2.d0*j-1.d0)*z*p2-(j-1.d0)*p3)/j 
11        continue 
          pp=n*(z*p1-p2)/(z*z-1.d0) 
          z1=z 
          z=z1-p1/pp 
        if(abs(z-z1).gt.EPS)goto 1 
        x(i)=xm-xl*z 
        x(n+1-i)=xm+xl*z 
        w(i)=2.d0*xl/((1.d0-z*z)*pp*pp) 
        w(n+1-i)=w(i) 
12    continue 
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
C  
      SUBROUTINE fleg(x,pl,nl) 
      INTEGER nl 
      REAL x,pl(nl) 
      INTEGER j 
      REAL d,f1,f2,twox 
      pl(1)=1. 
      pl(2)=x 
      if(nl.gt.2) then 
        twox=2.*x 
        f2=x 
        d=1. 
        do 11 j=3,nl 
          f1=d 
          f2=f2+twox 
          d=d+1. 
          pl(j)=(f2*pl(j-1)-f1*pl(j-2))/d 
11      continue 
      endif 
      return 
      END 
c       
c
c       svdfit(ndata,a,ma,u,b,cor) 
C this program performs least square fitting:
C
C        bb_i = a(1) * u_i(1) + a(2) * u_i(2) + ... + a(N) * u_i(N)
C                 (i=1,ndata) (N: ma)
C        so that   Sum ( b - bb )^2 is minimum
C
C input:
C
C         u_i(k); (k=1,ma; i=1,ndata)   the x values,
C                                 2-dimensional variables
C
C         b_i;          ( i=1,ndata )  the y values
C
C output:
C
C         a(i); i=1,ma
C
C         correlation coefficient:  cor
C                   (for statistical significance test)
C
c
      SUBROUTINE svdfit(ndata,a,ma,u,b,cor) 
      parameter (nn=1000,mm=301)
      PARAMETER (TOL=1.e-9) 
      INTEGER ma,ndata
      REAL cor,a(mm),u(nn,mm),v(mm,mm),
     $     w(mm),bb(nn),u0(nn,mm) 
      INTEGER i,j 
      REAL sum,thresh,wmax,b(nn),b0(nn) 
c
        do j=1,ma
         a(j) = 0.
        do i=1,ndata
         b0(i) = b(i)
         u0(i,j)=u(i,j)
        enddo
        enddo
c
c    evaluate the least square problem and sorting the eigenvalues
      call svdcmp(u,ndata,ma,nn,mm,w,v) 
c
c    finding the largest eigenvalues and the cutoff eigenvalues
      wmax=0. 
      do 13 j=1,ma 
        if(w(j).gt.wmax)wmax=w(j) 
13    continue 
      thresh=TOL*wmax 
c
c    zero the eigenvalues smaller than the cutoff values 
      do 14 j=1,ma 
        if(w(j).lt.thresh)w(j)=0. 
14    continue 
c
c    solve for a 
      call svbksb(u,w,v,ndata,ma,nn,mm,b,a) 
      do 16 i=1,ndata 
        bb(i) = 0.      
        do 15 j=1,ma 
         bb(i) = bb(i)+a(j)*u0(i,j) 
15      continue 
16    continue 
c
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
      FUNCTION pythag(a,b) 
      REAL a,b,pythag 
      REAL absa,absb 
      absa=abs(a) 
      absb=abs(b) 
      if(absa.gt.absb)then 
        pythag=absa*sqrt(1.+(absb/absa)**2) 
      else 
        if(absb.eq.0.)then 
          pythag=0. 
        else 
          pythag=absb*sqrt(1.+(absa/absb)**2) 
        endif 
      endif 
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
      SUBROUTINE svbksb(u,w,v,m,n,mp,np,b,x) 
      INTEGER m,mp,n,np,NMAX 
      REAL b(mp),u(mp,np),v(np,np),w(np),x(np) 
      PARAMETER (NMAX=10000) 
      INTEGER i,j,jj 
      REAL s,tmp(NMAX) 
      do 12 j=1,n 
        s=0. 
        if(w(j).ne.0.)then 
          do 11 i=1,m 
            s=s+u(i,j)*b(i) 
11        continue 
          s=s/w(j) 
        endif 
        tmp(j)=s 
12    continue 
      do 14 j=1,n 
        s=0. 
        do 13 jj=1,n 
          s=s+v(j,jj)*tmp(jj) 
13      continue 
        x(j)=s 
14    continue 
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
      SUBROUTINE svdcmp(a,m,n,mp,np,w,v) 
      INTEGER m,mp,n,np,NMAX 
      REAL a(mp,np),v(np,np),w(np) 
      PARAMETER (NMAX=500) 
CU    USES pythag 
      INTEGER i,its,j,jj,k,l,nm 
      REAL anorm,c,f,g,h,s,scale,x,y,z,rv1(NMAX),pythag 
      g=0.0 
      scale=0.0 
      anorm=0.0 
      do 25 i=1,n 
        l=i+1 
        rv1(i)=scale*g 
        g=0.0 
        s=0.0 
        scale=0.0 
        if(i.le.m)then 
          do 11 k=i,m 
            scale=scale+abs(a(k,i)) 
11        continue 
          if(scale.ne.0.0)then 
            do 12 k=i,m 
              a(k,i)=a(k,i)/scale 
              s=s+a(k,i)*a(k,i) 
12          continue 
            f=a(i,i) 
            g=-sign(sqrt(s),f) 
            h=f*g-s 
            a(i,i)=f-g 
            do 15 j=l,n 
              s=0.0 
              do 13 k=i,m 
                s=s+a(k,i)*a(k,j) 
13            continue 
              f=s/h 
              do 14 k=i,m 
                a(k,j)=a(k,j)+f*a(k,i) 
14            continue 
15          continue 
            do 16 k=i,m 
              a(k,i)=scale*a(k,i) 
16          continue 
          endif 
        endif 
        w(i)=scale *g 
        g=0.0 
        s=0.0 
        scale=0.0 
        if((i.le.m).and.(i.ne.n))then 
          do 17 k=l,n 
            scale=scale+abs(a(i,k)) 
17        continue 
          if(scale.ne.0.0)then 
            do 18 k=l,n 
              a(i,k)=a(i,k)/scale 
              s=s+a(i,k)*a(i,k) 
18          continue 
            f=a(i,l) 
            g=-sign(sqrt(s),f) 
            h=f*g-s 
            a(i,l)=f-g 
            do 19 k=l,n 
              rv1(k)=a(i,k)/h 
19          continue 
            do 23 j=l,m 
              s=0.0 
              do 21 k=l,n 
                s=s+a(j,k)*a(i,k) 
21            continue 
              do 22 k=l,n 
                a(j,k)=a(j,k)+s*rv1(k) 
22            continue 
23          continue 
            do 24 k=l,n 
              a(i,k)=scale*a(i,k) 
24          continue 
          endif 
        endif 
        anorm=max(anorm,(abs(w(i))+abs(rv1(i)))) 
25    continue 
      do 32 i=n,1,-1 
        if(i.lt.n)then 
          if(g.ne.0.0)then 
            do 26 j=l,n 
              v(j,i)=(a(i,j)/a(i,l))/g 
26          continue 
            do 29 j=l,n 
              s=0.0 
              do 27 k=l,n 
                s=s+a(i,k)*v(k,j) 
27            continue 
              do 28 k=l,n 
                v(k,j)=v(k,j)+s*v(k,i) 
28            continue 
29          continue 
          endif 
          do 31 j=l,n 
            v(i,j)=0.0 
            v(j,i)=0.0 
31        continue 
        endif 
        v(i,i)=1.0 
        g=rv1(i) 
        l=i 
32    continue 
      do 39 i=min(m,n),1,-1 
        l=i+1 
        g=w(i) 
        do 33 j=l,n 
          a(i,j)=0.0 
33      continue 
        if(g.ne.0.0)then 
          g=1.0/g 
          do 36 j=l,n 
            s=0.0 
            do 34 k=l,m 
              s=s+a(k,i)*a(k,j) 
34          continue 
            f=(s/a(i,i))*g 
            do 35 k=i,m 
              a(k,j)=a(k,j)+f*a(k,i) 
35          continue 
36        continue 
          do 37 j=i,m 
            a(j,i)=a(j,i)*g 
37        continue 
        else 
          do 38 j= i,m 
            a(j,i)=0.0 
38        continue 
        endif 
        a(i,i)=a(i,i)+1.0 
39    continue 
      do 49 k=n,1,-1 
        do 48 its=1,30 
          do 41 l=k,1,-1 
            nm=l-1 
            if((abs(rv1(l))+anorm).eq.anorm)  goto 2 
            if((abs(w(nm))+anorm).eq.anorm)  goto 1 
41        continue 
1         c=0.0 
          s=1.0 
          do 43 i=l,k 
            f=s*rv1(i) 
            rv1(i)=c*rv1(i) 
            if((abs(f)+anorm).eq.anorm) goto 2 
            g=w(i) 
            h=pythag(f,g) 
            w(i)=h 
            h=1.0/h 
            c= (g*h) 
            s=-(f*h) 
            do 42 j=1,m 
              y=a(j,nm) 
              z=a(j,i) 
              a(j,nm)=(y*c)+(z*s) 
              a(j,i)=-(y*s)+(z*c) 
42          continue 
43        continue 
2         z=w(k) 
          if(l.eq.k)then 
            if(z.lt.0.0)then 
              w(k)=-z 
              do 44 j=1,n 
                v(j,k)=-v(j,k) 
44            continue 
            endif 
            goto 3 
          endif 
          if(its.eq.30) then
            pause 'no convergence in svdcmp' 
          endif
          x=w(l) 
          nm=k-1 
          y=w(nm) 
          g=rv1(nm) 
          h=rv1(k) 
          f=((y-z)*(y+z)+(g-h)*(g+h))/(2.0*h*y) 
          g=pythag(f,1.0) 
          f=((x-z)*(x+z)+h*((y/(f+sign(g,f)))-h))/x 
          c=1.0 
          s=1.0 
          do 47 j=l,nm 
            i=j+1 
            g=rv1(i) 
            y=w(i) 
            h=s*g 
            g=c*g 
            z=pythag(f,h) 
            rv1(j)=z 
            c=f/z 
            s=h/z 
            f= (x*c)+(g*s) 
            g=-(x*s)+(g*c) 
            h=y*s 
            y=y*c 
            do 45 jj=1,n 
              x=v(jj,j) 
              z=v(jj,i) 
              v(jj,j)= (x*c)+(z*s) 
              v(jj,i)=-(x*s)+(z*c) 
45          continue 
            z=pythag(f,h) 
            w(j)=z 
            if(z.ne.0.0)then 
              z=1.0/z 
              c=f*z 
              s=h*z 
            endif 
            f= (c*g)+(s*y) 
            x=-(s*g)+(c*y) 
            do 46 jj=1,m 
              y=a(jj,j) 
              z=a(jj,i) 
              a(jj,j)= (y*c)+(z*s) 
              a(jj,i)=-(y*s)+(z*c) 
46          continue 
47        continue 
          rv1(l)=0.0 
          rv1(k)=f 
          w(k)=x 
48      continue 
3       continue 
49    continue 
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 
      SUBROUTINE svdvar(v,ma,np,w,cvm,ncvm) 
      INTEGER ma,ncvm,np,MMAX 
      REAL cvm(ncvm,ncvm),v(np,np),w(np) 
      PARAMETER (MMAX=20) 
      INTEGER i,j,k 
      REAL sum,wti(MMAX) 
      do 11 i=1,ma 
        wti(i)=0. 
        if(w(i).ne.0.) wti(i)=1./(w(i)*w(i)) 
11    continue 
      do 14 i=1,ma 
        do 13 j=1,i 
          sum=0. 
          do 12 k=1,ma 
            sum=sum+v(i,k)*v(j,k)*wti(k) 
12        continue 
          cvm(i,j)=sum 
          cvm(j,i)=sum 
13      continue 
14    continue 
      return 
      END 
C  (C) Copr. 1986-92 Numerical Recipes Software 71a. 

c
c
c   integration int y dx from x(1) to x(n)
c
c

