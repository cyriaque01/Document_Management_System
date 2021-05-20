/*==============================================================*/
/* Nom de SGBD :  PostgreSQL 8                                  */
/* Date de création :  05/20/21 9:40:10 PM                      */
/*==============================================================*/


drop index PERSON_CASHIER_FK;

drop index CASHIER_PK;

drop table CASHIER;

drop index REGISTER_PHARMACY_FK;

drop index PERSON_REGISTER_FK;

drop index CAHSIER_REGISTER_FK;

drop index CASHREGISTER_PK;

drop table CASHREGISTER;

drop index PRESON_DOC_FK;

drop index DOCTOR_PK;

drop table DOCTOR;

drop index LOGIN_PERSON_FK;

drop index LOGIN_PK;

drop table LOGIN;

drop index ASSOCIATION_10_FK;

drop index NURSE_PK;

drop table NURSE;

drop index PERSON_PATIENT_FK;

drop index PATIENT_PK;

drop table PATIENT;

drop index PATIENTBOOK_PK;

drop table PATIENTBOOK;

drop index PATIENT_BOOK2_FK;

drop index PATIENT_BOOK_FK;

drop index PATIENT_BOOK_PK;

drop table PATIENT_BOOK;

drop index PERSON_PK;

drop table PERSON;

drop index PHARMACY_PK;

drop table PHARMACY;

/*==============================================================*/
/* Table : CASHIER                                              */
/*==============================================================*/
create table CASHIER (
   ID_CASHIER           INT4                 not null,
   ID_PERSON            INT4                 not null,
   PASSWORD             VARCHAR(1024)        not null,
   HOURSSTART           DATE                 null,
   HOURSEND             DATE                 null,
   constraint PK_CASHIER primary key (ID_CASHIER)
);

/*==============================================================*/
/* Index : CASHIER_PK                                           */
/*==============================================================*/
create unique index CASHIER_PK on CASHIER (
ID_CASHIER
);

/*==============================================================*/
/* Index : PERSON_CASHIER_FK                                    */
/*==============================================================*/
create  index PERSON_CASHIER_FK on CASHIER (
ID_PERSON
);

/*==============================================================*/
/* Table : CASHREGISTER                                         */
/*==============================================================*/
create table CASHREGISTER (
   ID_TRANSACTION       INT4                 not null,
   ID_PRODUCT           INT4                 not null,
   ID_CASHIER           INT4                 not null,
   ID_PERSON            INT4                 not null,
   AMOUNT               DECIMAL(8)           null,
   DATE                 DATE                 null,
   constraint PK_CASHREGISTER primary key (ID_TRANSACTION)
);

/*==============================================================*/
/* Index : CASHREGISTER_PK                                      */
/*==============================================================*/
create unique index CASHREGISTER_PK on CASHREGISTER (
ID_TRANSACTION
);

/*==============================================================*/
/* Index : CAHSIER_REGISTER_FK                                  */
/*==============================================================*/
create  index CAHSIER_REGISTER_FK on CASHREGISTER (
ID_CASHIER
);

/*==============================================================*/
/* Index : PERSON_REGISTER_FK                                   */
/*==============================================================*/
create  index PERSON_REGISTER_FK on CASHREGISTER (
ID_PERSON
);

/*==============================================================*/
/* Index : REGISTER_PHARMACY_FK                                 */
/*==============================================================*/
create  index REGISTER_PHARMACY_FK on CASHREGISTER (
ID_PRODUCT
);

/*==============================================================*/
/* Table : DOCTOR                                               */
/*==============================================================*/
create table DOCTOR (
   ID_DOCTOR            INT4                 not null,
   ID_PERSON            INT4                 not null,
   SPECIALITY           VARCHAR(1024)        null,
   HOURSSTART           DATE                 null,
   HOURSEND             DATE                 null,
   constraint PK_DOCTOR primary key (ID_DOCTOR)
);

/*==============================================================*/
/* Index : DOCTOR_PK                                            */
/*==============================================================*/
create unique index DOCTOR_PK on DOCTOR (
ID_DOCTOR
);

/*==============================================================*/
/* Index : PRESON_DOC_FK                                        */
/*==============================================================*/
create  index PRESON_DOC_FK on DOCTOR (
ID_PERSON
);

/*==============================================================*/
/* Table : LOGIN                                                */
/*==============================================================*/
create table LOGIN (
   ID_LOGIN             INT4                 not null,
   ID_PERSON            INT4                 not null,
   USERNAME             VARCHAR(1)           not null,
   PASSWORD             VARCHAR(1024)        not null,
   constraint PK_LOGIN primary key (ID_LOGIN)
);

/*==============================================================*/
/* Index : LOGIN_PK                                             */
/*==============================================================*/
create unique index LOGIN_PK on LOGIN (
ID_LOGIN
);

/*==============================================================*/
/* Index : LOGIN_PERSON_FK                                      */
/*==============================================================*/
create  index LOGIN_PERSON_FK on LOGIN (
ID_PERSON
);

/*==============================================================*/
/* Table : NURSE                                                */
/*==============================================================*/
create table NURSE (
   ID_NURSE             INT4                 not null,
   ID_PERSON            INT4                 not null,
   HOURSSTART           DATE                 null,
   HOURSEND             DATE                 null,
   constraint PK_NURSE primary key (ID_NURSE)
);

/*==============================================================*/
/* Index : NURSE_PK                                             */
/*==============================================================*/
create unique index NURSE_PK on NURSE (
ID_NURSE
);

/*==============================================================*/
/* Index : ASSOCIATION_10_FK                                    */
/*==============================================================*/
create  index ASSOCIATION_10_FK on NURSE (
ID_PERSON
);

/*==============================================================*/
/* Table : PATIENT                                              */
/*==============================================================*/
create table PATIENT (
   ID_PATIENT           INT4                 not null,
   ID_PERSON            INT4                 not null,
   DATE                 DATE                 null,
   ROOMNUMBER           INT4                 null,
   CHECKOUT             DATE                 null,
   DIAGNOSIS            VARCHAR(1024)        null,
   constraint PK_PATIENT primary key (ID_PATIENT)
);

/*==============================================================*/
/* Index : PATIENT_PK                                           */
/*==============================================================*/
create unique index PATIENT_PK on PATIENT (
ID_PATIENT
);

/*==============================================================*/
/* Index : PERSON_PATIENT_FK                                    */
/*==============================================================*/
create  index PERSON_PATIENT_FK on PATIENT (
ID_PERSON
);

/*==============================================================*/
/* Table : PATIENTBOOK                                          */
/*==============================================================*/
create table PATIENTBOOK (
   ID_PATIENTBOOK       INT4                 not null,
   DEPARTEMENT          VARCHAR(1024)        null,
   DESCRIPTION          VARCHAR(8000)        null,
   DATE                 DATE                 null,
   RESULTATS            VARCHAR(8000)        null,
   constraint PK_PATIENTBOOK primary key (ID_PATIENTBOOK)
);

/*==============================================================*/
/* Index : PATIENTBOOK_PK                                       */
/*==============================================================*/
create unique index PATIENTBOOK_PK on PATIENTBOOK (
ID_PATIENTBOOK
);

/*==============================================================*/
/* Table : PATIENT_BOOK                                         */
/*==============================================================*/
create table PATIENT_BOOK (
   ID_PATIENT           INT4                 not null,
   ID_PATIENTBOOK       INT4                 not null,
   constraint PK_PATIENT_BOOK primary key (ID_PATIENT, ID_PATIENTBOOK)
);

/*==============================================================*/
/* Index : PATIENT_BOOK_PK                                      */
/*==============================================================*/
create unique index PATIENT_BOOK_PK on PATIENT_BOOK (
ID_PATIENT,
ID_PATIENTBOOK
);

/*==============================================================*/
/* Index : PATIENT_BOOK_FK                                      */
/*==============================================================*/
create  index PATIENT_BOOK_FK on PATIENT_BOOK (
ID_PATIENT
);

/*==============================================================*/
/* Index : PATIENT_BOOK2_FK                                     */
/*==============================================================*/
create  index PATIENT_BOOK2_FK on PATIENT_BOOK (
ID_PATIENTBOOK
);

/*==============================================================*/
/* Table : PERSON                                               */
/*==============================================================*/
create table PERSON (
   ID_PERSON            INT4                 not null,
   NAME                 VARCHAR(1024)        null,
   SURNAME              VARCHAR(1024)        null,
   TYPE                 CHAR(256)            null,
   PHONE                VARCHAR(1024)        null,
   POBOX                VARCHAR(1024)        null,
   EMAIL                VARCHAR(1024)        null,
   HOME                 VARCHAR(1024)        null,
   constraint PK_PERSON primary key (ID_PERSON)
);

/*==============================================================*/
/* Index : PERSON_PK                                            */
/*==============================================================*/
create unique index PERSON_PK on PERSON (
ID_PERSON
);

/*==============================================================*/
/* Table : PHARMACY                                             */
/*==============================================================*/
create table PHARMACY (
   ID_PRODUCT           INT4                 not null,
   NAME                 VARCHAR(1024)        null,
   PRICE                DECIMAL              null,
   STOCK                INT4                 null,
   constraint PK_PHARMACY primary key (ID_PRODUCT)
);

/*==============================================================*/
/* Index : PHARMACY_PK                                          */
/*==============================================================*/
create unique index PHARMACY_PK on PHARMACY (
ID_PRODUCT
);

alter table CASHIER
   add constraint FK_CASHIER_PERSON_CA_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table CASHREGISTER
   add constraint FK_CASHREGI_CAHSIER_R_CASHIER foreign key (ID_CASHIER)
      references CASHIER (ID_CASHIER)
      on delete restrict on update restrict;

alter table CASHREGISTER
   add constraint FK_CASHREGI_PERSON_RE_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table CASHREGISTER
   add constraint FK_CASHREGI_REGISTER__PHARMACY foreign key (ID_PRODUCT)
      references PHARMACY (ID_PRODUCT)
      on delete restrict on update restrict;

alter table DOCTOR
   add constraint FK_DOCTOR_PRESON_DO_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table LOGIN
   add constraint FK_LOGIN_LOGIN_PER_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table NURSE
   add constraint FK_NURSE_ASSOCIATI_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table PATIENT
   add constraint FK_PATIENT_PERSON_PA_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table PATIENT_BOOK
   add constraint FK_PATIENT__PATIENT_B_PATIENT foreign key (ID_PATIENT)
      references PATIENT (ID_PATIENT)
      on delete restrict on update restrict;

alter table PATIENT_BOOK
   add constraint FK_PATIENT__PATIENT_B_PATIENTB foreign key (ID_PATIENTBOOK)
      references PATIENTBOOK (ID_PATIENTBOOK)
      on delete restrict on update restrict;

