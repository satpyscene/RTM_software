      PROGRAM   AVERAGE_WATER
       
      DOUBLE PRECISION :: WVL(51),REFR(51),REFI(51),WL(10),WWW
      DOUBLE PRECISION :: WL_SRF(10000),W_SRF(10000),W_T
      DOUBLE PRECISION :: R,QE,SA,AF,V,S
      DOUBLE PRECISION :: ANG(498),P11(498),P22(498),P33(498),&
                                   P44(498),P12(498),P43(498)
      DOUBLE PRECISION :: W_SC,WL1(1900),WL2(1900),WW(1900),WEIGHT,NORM
      DOUBLE PRECISION :: INT_P11(90,498),INT_P22(90,498),INT_P33(90,498),&
                          INT_P44(90,498),INT_P12(90,498),INT_P43(90,498)
      DOUBLE PRECISION :: INT_QE(90),INT_AF(90),INT_SA(90)
      DOUBLE PRECISION :: WL_START,WL_END,WL_0,WL_MIN,WL_MAX,D_WL
      INTEGER :: RE(90)
      INTEGER :: I,SIZE_WVN,N_WL,FIND_END,n_re,n_band,n_ag
      CHARACTER :: DIR*50,FILENAME*8,F_NAME_WL*30,FULLNAME*100
      character*100 inDir, outDir

      call getarg(1,inDir)
      call getarg(2,outDir)

      ! read re
      open(112, file='./INPUT/input_re.dat',status='unknown')
      read(112, *) n_re
      do i=1,n_re
        read(112, *) RE(I)
      end do
      close(112)

      n_ag=498
!      SIZE_WVN = 445 
      N_SIZE_DIS = 90

      OPEN(UNIT=1,FILE='./DATABASE/Solar_Constant.dat',STATUS='OLD')
      READ(1,*) (WL1(I),WL2(I),WW(I),I=1,1900,1)
      CLOSE(1)
       
      OPEN(UNIT=1,FILE='./INPUT/input_band.dat',STATUS='OLD')
      READ(1,*)  n_band
    
      DO I=1, n_band

         INT_QE = 0.0D0
         INT_SA = 0.0D0
         INT_AF = 0.0D0
         INT_P11 = 0.0D0
         INT_P22 = 0.0D0
         INT_P33 = 0.0D0
         INT_P44 = 0.0D0
         INT_P12 = 0.0D0
         INT_P43 = 0.0D0
         NORM = 0.0D0
    
         READ(1,'(A8,3F7.2)')  FILENAME,WL_START,D_WL,WL_END
!         WRITE(*,*) FILENAME
         N_WL = 1 + INT((WL_END-WL_START)/D_WL+0.000001)
         OPEN (UNIT=3,FILE="./DATABASE/SRF/"//FILENAME//".SRF", &
               STATUS='OLD')

         K=1
         DO 
            READ(3,*,IOSTAT=FIND_END)  WL_SRF(K),W_SRF(K)
            IF(FIND_END.LT.0.0D0) EXIT
            K=K+1
         ENDDO
         N_SRF = K-1
         CLOSE(3)

         DO  J=1,N_WL

            WL_0 = WL_START + DBLE(J-1)*D_WL
            WL_MIN = WL_0 - D_WL*0.5D0 
            WL_MAX = WL_0 + D_WL*0.5D0 

            WRITE(F_NAME_WL,"(F10.2)") WL_0

            DO K=1,30
               LA1=K
               IF(F_NAME_WL(K:K) /= " ") EXIT
            END DO

            DO K=30,1,-1
               LA2 = K
               IF(F_NAME_WL(K:K) /= " ") EXIT
            END DO

            DO K = LA1, LA2
               IF(F_NAME_WL(K:K) == ".") F_NAME_WL(K:K) = "p"
            END DO
!            WRITE(*,*) F_NAME_WL
!            W_SC = 0.0D0
!            DO K=1,1900
!               IF ((WL2(K).GT.WL_MIN).AND.(WL1(K).LE.WL_MIN)) THEN
!                  CALL
!                  GET_SRF(N_SRF,WL_SRF,W_SRF,(WL2(K)+WL_MIN)*0.5D0,W_T)
!                  W_SC = W_SC +
!                  WW(K)*(WL2(K)-WL_MIN)/(WL2(K)-WL1(K))*W_T
!               ELSEIF ((WL1(K).GT.WL_MIN).AND.(WL2(K).LE.WL_MAX)) THEN
!                  CALL
!                  GET_SRF(N_SRF,WL_SRF,W_SRF,(WL2(K)+WL1(K))*0.5D0,W_T)
!                  W_SC = W_SC + WW(K)*W_T
!               ELSEIF ((WL2(K).GT.WL_MAX).AND.(WL1(K).LE.WL_MAX)) THEN
!                  CALL
!                  GET_SRF(N_SRF,WL_SRF,W_SRF,(WL1(K)+WL_MAX)*0.5D0,W_T)
!                  W_SC = W_SC +
!                  WW(K)*(WL_MAX-WL1(K))/(WL2(K)-WL1(K))*W_T
!               ELSEIF (WL1(K).GT.WL_MAX) THEN
!                  EXIT
!               ENDIF
!               WRITE(100,*) WL1(K),WL2(K),W_T 
!            ENDDO
!            NORM = NORM + W_SC

            W_SC = 0.0D0
            DO K=1,N_SRF
              IF (WL_SRF(K).GT.WL_MIN.AND.WL_SRF(K).LE.WL_MAX) THEN
                DO KK=1,1900
                  IF ((WL2(KK).GE.WL_SRF(K)).AND.(WL1(KK).LT.WL_SRF(K))) THEN
                    W_SC = W_SC + W_SRF(K)*WW(KK)
                    GOTO 100
                  ENDIF
                ENDDO
              ENDIF
100         ENDDO
            NORM = NORM + W_SC
           
            DO K=1,n_re
            WRITE(FULLNAME,'(3A,I3.3,A)') &
                    'WVN_', F_NAME_WL(LA1:LA2),'_DE_',RE(K),'.dat'
            OPEN(UNIT=3,FILE=TRIM(inDir)//TRIM(FULLNAME),STATUS='OLD')
            READ(3,581)  R, V, S, QE, SA, AF
            DO KKK=1,n_ag
               READ(3,1005) ANG(KKK),P11(KKK),P22(KKK),P33(KKK),&
                                     P44(KKK),P12(KKK),P43(KKK)
            ENDDO
            CLOSE(3)
  
            INT_QE(K)  =  INT_QE(K) + W_SC*QE
            INT_SA(K)  =  INT_SA(K) + W_SC*QE*SA
            INT_AF(K)  =  INT_AF(K) + W_SC*QE*SA*AF
         
!            WRITE(*,*) K,INT_P11(K,1)

            INT_P11(K,1:498) = INT_P11(K,1:498) + W_SC*QE*SA*P11(1:498)
            INT_P22(K,1:498) = INT_P22(K,1:498) + W_SC*QE*SA*P22(1:498)
            INT_P33(K,1:498) = INT_P33(K,1:498) + W_SC*QE*SA*P33(1:498)
            INT_P44(K,1:498) = INT_P44(K,1:498) + W_SC*QE*SA*P44(1:498)
            INT_P12(K,1:498) = INT_P12(K,1:498) + W_SC*QE*SA*P12(1:498)
            INT_P43(K,1:498) = INT_P43(K,1:498) + W_SC*QE*SA*P43(1:498)
             
            ENDDO
            WRITE(*,*) WL_0,W_SC
         ENDDO
         CLOSE(2)
  

         DO K=1,n_re

         INT_P22(K,1:498) = INT_P22(K,1:498)/INT_P11(K,1:498)
         INT_P33(K,1:498) = INT_P33(K,1:498)/INT_P11(K,1:498)
         INT_P44(K,1:498) = INT_P44(K,1:498)/INT_P11(K,1:498)
         INT_P12(K,1:498) = INT_P12(K,1:498)/INT_P11(K,1:498)
         INT_P43(K,1:498) = INT_P43(K,1:498)/INT_P11(K,1:498)

         INT_P11(K,1:498) = INT_P11(K,1:498)/INT_SA(K)
         INT_AF(K) = INT_AF(K)/INT_SA(K)
         INT_SA(K) = INT_SA(K)/INT_QE(K)
         INT_QE(K) = INT_QE(K)/NORM

         WRITE(FULLNAME,'(2A,I3.3,A)') FILENAME,'_DE_',RE(K),'.dat'
!         WRITE(*,*) FULLNAME
         OPEN(UNIT=4,FILE=TRIM(outDir)//TRIM(FULLNAME),STATUS='UNKNOWN')
         WRITE(4,581) DBLE(K),V,S,INT_QE(K),INT_SA(K),INT_AF(K)
         DO KK=1,498
!            WRITE(4,1004) ANG(KK),INT_P11(K,KK)
            WRITE(4,1005) ANG(KK),INT_P11(K,KK),INT_P22(K,KK),INT_P33(K,KK),&
                                  INT_P44(K,KK),INT_P12(K,KK),INT_P43(K,KK)
         ENDDO
         CLOSE(4)
         ENDDO
      ENDDO


  580 FORMAT(4F12.4)
  581 FORMAT(F10.2,5E18.8)
 1004 FORMAT(' ',F6.2,E20.6)
 1005 FORMAT(F10.3,6E20.8)

      END PROGRAM


      SUBROUTINE GET_SRF(N_SRF,WL_SRF,W_SRF,W0,W_T)
      INTEGER N_SRF,I
      DOUBLE PRECISION WL_SRF(N_SRF),W_SRF(N_SRF),W0,W_T
      DO I=1,N_SRF-1
         IF ((WL_SRF(I).LE.W0).AND.(WL_SRF(I+1).GE.W0)) THEN
            W_T = W_SRF(I) + ( W_SRF(I+1)- W_SRF(I))*(W0-WL_SRF(I))/     &
                             (WL_SRF(I+1)-WL_SRF(I))

            EXIT
         ENDIF
      ENDDO
      RETURN
      END SUBROUTINE GET_SRF

