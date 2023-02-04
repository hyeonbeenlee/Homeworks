clc;format short
ABT=[9.2542e-01   1.8028e-02   3.7852e-01   1.0000e+00
   1.6318e-01   8.8256e-01  -4.4097e-01   2.0000e+00
  -3.4202e-01   4.6985e-01   8.1380e-01   3.0000e+00
            0            0            0   1.0000e+00];
BCT=[9.3969e-01            0   3.4202e-01   3.0000e+00
            0   1.0000e+00            0            0
  -3.4202e-01            0   9.3969e-01   1.0000e+00
            0            0            0   1.0000e+00];

ABR=ABT(1:3,1:3);
BCR=BCT(1:3,1:3);
ACR=ABR*BCR;
P1=ABT(1:3,4); %{A}·Î Ç¥ÇöµÊ
P2=BCT(1:3,4); %{B}·Î Ç¥ÇöµÊ
P2=ABR*P2;
ACT=[ACR P1+P2;0 0 0 1];
CAT=[ACR' -ACR'*(P1+P2);0 0 0 1];


%Obtain ABT from ACT and BCT
BCRinv=BCR'; %orthogonality
obt_ABR=ACR*BCRinv;
APCORG=ACT(1:3,4);
BPCORG=BCT(1:3,4);
obt_APBORG=APCORG-ABR*BPCORG;
obt_ABT=[obt_ABR obt_APBORG;0 0 0 1];

%Obtain BCT from ACT and ABT
ABRinv=ABR';
obt_BCR=ABRinv*ACR;
APBORG=ABT(1:3,4);
obt_BPCORG=ABRinv*(APCORG-APBORG);
obt_BCT=[obt_BCR obt_BPCORG;0 0 0 1];

