!!!!!!!!!!!!!!!!!!!!!!!!!!!   该程序是假设1-90um冰的single_to_bulk   !!!!!!!!!!!!!!!!!!!!!!!!!
      PROGRAM AVERAGE 

      INTEGER,PARAMETER :: n_ag = 498 ! number of angle
      INTEGER,PARAMETER :: n_rs = 189 ! number of rsize(original)
      INTEGER,PARAMETER :: n_ri = 90  ! number of rsize(integrated)  根据需求
      ! INTEGER, PARAMETER :: PREC = SELECTED_REAL_KIND(15, 307)
      DOUBLE PRECISION P11(n_rs,n_ag),QE(n_rs),G(n_rs),SSA(n_rs)
      DOUBLE PRECISION P12(n_rs,n_ag),P12_AVE(n_ag)
      DOUBLE PRECISION P22(n_rs,n_ag),P22_AVE(n_ag)
      DOUBLE PRECISION P33(n_rs,n_ag),P33_AVE(n_ag)
      DOUBLE PRECISION P43(n_rs,n_ag),P43_AVE(n_ag)
      DOUBLE PRECISION P44(n_rs,n_ag),P44_AVE(n_ag)
      DOUBLE PRECISION ANG(n_ag),P11_AVE(n_ag),Q_AVE,G_AVE,SSA_AVE
      DOUBLE PRECISION WL,SIZE(n_rs),VOLUM(n_rs),PAREA(n_rs)
      DOUBLE PRECISION NORM,RE,R_E,V1,V2,V3
!      CHARACTER*150 DIR
      CHARACTER*150 inDir, outDir
      CHARACTER*100 F_NAME
      CHARACTER*30 F_WL
      CHARACTER*3 F_SIZE(n_ri)      ! set number of ouputfile (number of DEFF = 60)

      CHARACTER(len=32) :: fmt

      INTEGER I,III,IJK,LA1,LA2,n_re,n_wn,d_type
      INTEGER :: RADII(90)     ! set DEFF from 1 to 60 micron
!      INTEGER :: RADII(20)
!      !DATA RADII/2,4,6,8,10,12,14,16,18,20,             &
!                  24,28,32,36,40,44,48,52,56,60/
!      WRITE(*,*) RADII
!      WRITE(*,*) '(SIZE(RADII):)',SIZE(RADII)
!      WRITE(*,*) '(SIZE(RADII):)',SIZE(RADII,dim=2)
 
!      WRITE(DIR,*)  '/student/home/hljoy/FORWARD_RTM/RTM_learn/RTM_IW/DA&
!     &TA/' !当前目录下

!************************************* 获取输入参数********************
      call getarg(1,inDir)
      call getarg(2,outDir)

      open(112, file='./INPUT/input_re.dat',status='unknown')
      read(112, *) n_re
      do i=1,n_re
        read(112, *) RADII(I)
      end do
      close(112)

      DO I = 1, n_re
        WRITE(F_SIZE(I), '(I3.3)') RADII(I)  ! 将 1-60 存入 F_SIZE 中为 001, 002, 060
      ENDDO

      open(112, file='./INPUT/wl.dat',status='unknown')
      read(112, *) n_wn
      close(112)

      open(112, file='./INPUT/input.txt',status='unknown')
      do i=1,4
        read(112,*)
      end do
      read(112,*)  d_type, V1, V2, V3


      OPEN(UNIT=10,FILE=TRIM(inDir)//'isca.dat',STATUS='OLD')
      OPEN(UNIT=11,FILE=TRIM(inDir)//'P11.dat', STATUS='OLD')
      OPEN(UNIT=12,FILE=TRIM(inDir)//'P12.dat', STATUS='OLD')
      OPEN(UNIT=13,FILE=TRIM(inDir)//'P22.dat', STATUS='OLD')
      OPEN(UNIT=14,FILE=TRIM(inDir)//'P33.dat', STATUS='OLD')
      OPEN(UNIT=15,FILE=TRIM(inDir)//'P43.dat', STATUS='OLD')
      OPEN(UNIT=16,FILE=TRIM(inDir)//'P44.dat', STATUS='OLD')

      READ(11,*) ANG(1:n_ag)  !!!!!读取角度一行，剩下p11
      READ(12,*)
      READ(13,*)
      READ(14,*)
      READ(15,*)
      READ(16,*)

!************************************* 循环读取光学特性********************
      DO IJK=1,n_wn   ! wave length  callbhmie得到的
!************* 命名方式1 *************
!      WRITE(F_WL,'(I5.5)') IJK      
!      WRITE(*,*) F_WL  !00001-00004 
!*************************************
      ! DO I=1,n_rs    ! partical scale
      !    READ(10,"(7ES18.8)") WL,SIZE(I),VOLUM(I),PAREA(I),QE(I),SSA(I),G(I)
      !    QE(I)= QE(I)*PAREA(I)
      !    READ(11,"(<n_ag>ES18.8)") P11(I,1:n_ag)
      !    READ(12,"(<n_ag>ES18.8)") P12(I,1:n_ag)
      !    READ(13,"(<n_ag>ES18.8)") P22(I,1:n_ag)
      !    READ(14,"(<n_ag>ES18.8)") P33(I,1:n_ag)
      !    READ(15,"(<n_ag>ES18.8)") P43(I,1:n_ag)
      !    READ(16,"(<n_ag>ES18.8)") P44(I,1:n_ag)
      ! ENDDO
      ! 构造格式字符串
      
      DO I=1,n_rs    ! 颗粒尺度
            READ(10,"(7ES18.8)") WL, SIZE(I), VOLUM(I), PAREA(I), QE(I), SSA(I), G(I)
            QE(I) = QE(I) * PAREA(I)
        
            
            WRITE(fmt, '("(", I0, "ES18.8)")') n_ag
        
            ! 使用构造的格式字符串读取数据
            READ(11, fmt) P11(I, 1:n_ag)
            READ(12, fmt) P12(I, 1:n_ag)
            READ(13, fmt) P22(I, 1:n_ag)
            READ(14, fmt) P33(I, 1:n_ag)
            READ(15, fmt) P43(I, 1:n_ag)
            READ(16, fmt) P44(I, 1:n_ag)
      ENDDO

!***********命名方式2 0p55 ***************
      WRITE(F_WL,'(F10.2)') WL
!      WRITE(*,*) F_WL
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
!********************************************

      DO III=1,n_re !SIZE(RADII)

      P11_AVE  = 0.0D0
      P12_AVE  = 0.0D0
      P22_AVE  = 0.0D0
      P33_AVE  = 0.0D0
      P43_AVE  = 0.0D0
      P44_AVE  = 0.0D0
      Q_AVE    = 0.0D0
      SSA_AVE  = 0.0D0
      G_AVE    = 0.0D0
      AREA_AVE = 0.0D0
      VOLUME_AVE = 0.0D0
      NORM     = 0.0D0

      R_E = DBLE(RADII(III)) !1-60

!      V1 = 0.1D0

!**************** 积分********************
      DO I=2,n_rs-1

         RE= 0.75D0*VOLUM(I)/PAREA(I)
!         RE=SIZE(I)

!         ALPHA = (R_E*B)**((2.0D0*B-1.0D0)/B)/         &
!                 EXP(LOG(GAMMA((1.0D0-2.0D0*B)/B)))
!         T = RE**((1.0D0-3.0D0*B)/B)
!         PDF = ALPHA * T * DEXP(-(RE/(R_E*B)))
         if (d_type == 1) then
           call GAMMA_DISTRIBUTION(RE, R_E, V1, PDF)
         elseif (d_type == 2) then
           call LOG_NORMAL(RE, R_E, V1, PDF)
         end if

         NORM = NORM + PDF

         AREA_AVE = AREA_AVE + PDF*PAREA(I) !平均投影截面
         VOLUME_AVE = VOLUME_AVE + PDF*VOLUM(I)
         Q_AVE = Q_AVE + PDF*QE(I)
         SSA_AVE = SSA_AVE + PDF*QE(I)*SSA(I) 
         G_AVE = G_AVE + PDF*QE(I)*SSA(I)*G(I)
         P11_AVE(1:n_ag) = P11_AVE(1:n_ag) + PDF*QE(I)*SSA(I)*P11(I,1:n_ag)
         P12_AVE(1:n_ag) = P12_AVE(1:n_ag) + PDF*QE(I)*SSA(I)*P12(I,1:n_ag)
         P22_AVE(1:n_ag) = P22_AVE(1:n_ag) + PDF*QE(I)*SSA(I)*P22(I,1:n_ag)
         P33_AVE(1:n_ag) = P33_AVE(1:n_ag) + PDF*QE(I)*SSA(I)*P33(I,1:n_ag)
         P43_AVE(1:n_ag) = P43_AVE(1:n_ag) + PDF*QE(I)*SSA(I)*P43(I,1:n_ag)
         P44_AVE(1:n_ag) = P44_AVE(1:n_ag) + PDF*QE(I)*SSA(I)*P44(I,1:n_ag)

      ENDDO

      P12_AVE(1:n_ag) = P12_AVE(1:n_ag)/P11_AVE(1:n_ag)
      P22_AVE(1:n_ag) = P22_AVE(1:n_ag)/P11_AVE(1:n_ag)
      P33_AVE(1:n_ag) = P33_AVE(1:n_ag)/P11_AVE(1:n_ag)
      P43_AVE(1:n_ag) = P43_AVE(1:n_ag)/P11_AVE(1:n_ag)
      P44_AVE(1:n_ag) = P44_AVE(1:n_ag)/P11_AVE(1:n_ag)

      P11_AVE(1:n_ag) = P11_AVE(1:n_ag)/SSA_AVE
      G_AVE = G_AVE/SSA_AVE
      SSA_AVE = SSA_AVE/Q_AVE  ! Q_AVE=C_AVE
      Q_AVE = Q_AVE/AREA_AVE   ! 是Qext!
      VOLUME_AVE = VOLUME_AVE/NORM
      AREA_AVE = AREA_AVE/NORM 
      WRITE(F_NAME,'(5A)') 'WVN_',F_WL(LA1:LA2),"_DE_", &
                           F_SIZE(III),".dat"            !方式2写入
!      WRITE(F_NAME,'(5A)') 'WVN_',TRIM(F_WL),"_DE_", &
!                           F_SIZE(III),".dat"           !方式1写入
!      WRITE(*,*) F_NAME
      OPEN(UNIT=1,FILE=TRIM(outDir)//TRIM(F_NAME),STATUS='UNKNOWN')
      WRITE(1,581)  RADII(III)*1.0D0,VOLUME_AVE,AREA_AVE,&
                    Q_AVE,SSA_AVE,G_AVE

!      WRITE(1,'(A10,E16.10)') 'Qext    = ',Q_AVE
!      WRITE(1,'(A10,E16.10)') 'Qabs    = ',Q_AVE*(1.0D0-SSA_AVE)
!      WRITE(1,'(A10,E16.10)') 'Qsca    = ',Q_AVE*SSA_AVE
!      WRITE(1,'(A10,E16.10)') 'Albedo  = ',SSA_AVE
!      WRITE(1,'(A10,E16.10)') 'Parea   = ',AREA_AVE
!      WRITE(1,'(A10,E16.10)') 'Volume  = ',VOLUME_AVE
!      WRITE(1,'(A10,E16.10)') 'Gfactor = ',G_AVE

      DO J=1,n_ag
!      WRITE(1,"(F10.3,E20.8)") ANG(J),P11_AVE(J)
      WRITE(1,1005) ANG(J),P11_AVE(J),P22_AVE(J),P33_AVE(J), &
                    P44_AVE(J),P12_AVE(J),P43_AVE(J)
      ENDDO
      CLOSE(1)

      ENDDO
      ENDDO
 581  FORMAT(F10.2,5E18.8)
1005  FORMAT(F10.3,6E20.8)
7200  FORMAT(1X, 2(ES13.6, 1x), 2(ES13.6, 1x), 3(F8.4, 1x))

      END PROGRAM AVERAGE 

      function gamma(z)
      implicit real*8(a-h,o-z)
      data ti,nstep /0.d0,20001/
      f(t)=t**(z-1.d0)*dexp(-t)
      tf=30.d0
      dt=(tf-ti)/dfloat(nstep)
      sum=dt**z/z -dt**(z+1.d0)/(z+1.d0)
      do 10 i=2,nstep,2
      t=ti+dt*dfloat(i)
      sum=sum+(dt/3.d0)*(f(t-dt)+ 4.d0*f(t) +f(t+dt))
10    continue
      gamma=sum
      return
      end

      SUBROUTINE GAMMA_DISTRIBUTION(R, R_E, B, PDF)
        DOUBLE PRECISION RE,R_E
        DOUBLE PRECISION B,R,ALPHA,T
        REAL PDF
        ALPHA = (R_E*B)**((2.0D0*B-1.0D0)/B)/         &
               EXP(LOG(GAMMA((1.0D0-2.0D0*B)/B)))
        T = R**((1.0D0-3.0D0*B)/B)
        PDF = ALPHA * T * DEXP(-(R/(R_E*B)))
      END SUBROUTINE GAMMA_DISTRIBUTION

      SUBROUTINE LOG_NORMAL(R, R_E, SIGMA, PDF)
        DOUBLE PRECISION, PARAMETER :: PI = 3.141592653589793238462643d0
        DOUBLE PRECISION RE,R_E
        DOUBLE PRECISION SIGMA,R,ALPHA,T
        REAL PDF
        T = 1 / (2*PI)**(1/2) / SIGMA / R
        PDF = T * DEXP(-(LOG(R)-LOG(R_E))**2 / (2*SIGMA**2))
      END SUBROUTINE LOG_NORMAL

