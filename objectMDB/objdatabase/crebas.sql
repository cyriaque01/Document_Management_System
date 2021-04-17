/*==============================================================*/
/* Nom de SGBD :  PostgreSQL 8                                  */
/* Date de création :  04/18/21 12:42:39 AM                     */
/*==============================================================*/


drop index PERSON_ADRESSE_FK;

drop index ADRESSE_PK;

drop table ADRESSE;

drop index PRESONNE_DOC_FK;

drop index DOCTEUR_PK;

drop table DOCTEUR;

drop index PATIENTBOOK_PK;

drop table PATIENTBOOK;

drop index PERSON_PK;

drop table PERSON;

drop index PERSON_BOOK2_FK;

drop index PERSON_BOOK_FK;

drop index PERSON_BOOK_PK;

drop table PERSON_BOOK;

/*==============================================================*/
/* Table : ADRESSE                                              */
/*==============================================================*/
create table ADRESSE (
   ID_ADRESS            INT4                 not null,
   ID_PERSON            INT4                 not null,
   PHONE                VARCHAR(1024)        null,
   POBOX                VARCHAR(1024)        null,
   EMAIL                VARCHAR(1024)        null,
   HOME                 VARCHAR(1024)        null,
   constraint PK_ADRESSE primary key (ID_ADRESS)
);

/*==============================================================*/
/* Index : ADRESSE_PK                                           */
/*==============================================================*/
create unique index ADRESSE_PK on ADRESSE (
ID_ADRESS
);

/*==============================================================*/
/* Index : PERSON_ADRESSE_FK                                    */
/*==============================================================*/
create  index PERSON_ADRESSE_FK on ADRESSE (
ID_PERSON
);

/*==============================================================*/
/* Table : DOCTEUR                                              */
/*==============================================================*/
create table DOCTEUR (
   ID_DOCTOR            INT4                 not null,
   ID_PERSON            INT4                 not null,
   SPECIALITY           VARCHAR(1024)        null,
   HOURSSTART           DATE                 null,
   HOURSEND             DATE                 null,
   constraint PK_DOCTEUR primary key (ID_DOCTOR)
);

/*==============================================================*/
/* Index : DOCTEUR_PK                                           */
/*==============================================================*/
create unique index DOCTEUR_PK on DOCTEUR (
ID_DOCTOR
);

/*==============================================================*/
/* Index : PRESONNE_DOC_FK                                      */
/*==============================================================*/
create  index PRESONNE_DOC_FK on DOCTEUR (
ID_PERSON
);

/*==============================================================*/
/* Table : PATIENTBOOK                                          */
/*==============================================================*/
create table PATIENTBOOK (
   ID_PATIENTBOOK       INT4                 not null,
   LOCATION             VARCHAR(1024)        null,
   constraint PK_PATIENTBOOK primary key (ID_PATIENTBOOK)
);

/*==============================================================*/
/* Index : PATIENTBOOK_PK                                       */
/*==============================================================*/
create unique index PATIENTBOOK_PK on PATIENTBOOK (
ID_PATIENTBOOK
);

/*==============================================================*/
/* Table : PERSON                                               */
/*==============================================================*/
create table PERSON (
   ID_PERSON            INT4                 not null,
   NAME                 VARCHAR(1024)        null,
   SURNAME              VARCHAR(1024)        null,
   ADRESSE              INT4                 null,
   TYPE                 CHAR(256)            null,
   constraint PK_PERSON primary key (ID_PERSON)
);

/*==============================================================*/
/* Index : PERSON_PK                                            */
/*==============================================================*/
create unique index PERSON_PK on PERSON (
ID_PERSON
);

/*==============================================================*/
/* Table : PERSON_BOOK                                          */
/*==============================================================*/
create table PERSON_BOOK (
   ID_PERSON            INT4                 not null,
   ID_PATIENTBOOK       INT4                 not null,
   constraint PK_PERSON_BOOK primary key (ID_PERSON, ID_PATIENTBOOK)
);

/*==============================================================*/
/* Index : PERSON_BOOK_PK                                       */
/*==============================================================*/
create unique index PERSON_BOOK_PK on PERSON_BOOK (
ID_PERSON,
ID_PATIENTBOOK
);

/*==============================================================*/
/* Index : PERSON_BOOK_FK                                       */
/*==============================================================*/
create  index PERSON_BOOK_FK on PERSON_BOOK (
ID_PERSON
);

/*==============================================================*/
/* Index : PERSON_BOOK2_FK                                      */
/*==============================================================*/
create  index PERSON_BOOK2_FK on PERSON_BOOK (
ID_PATIENTBOOK
);

alter table ADRESSE
   add constraint FK_ADRESSE_PERSON_AD_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table DOCTEUR
   add constraint FK_DOCTEUR_PRESONNE__PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table PERSON_BOOK
   add constraint FK_PERSON_B_PERSON_BO_PERSON foreign key (ID_PERSON)
      references PERSON (ID_PERSON)
      on delete restrict on update restrict;

alter table PERSON_BOOK
   add constraint FK_PERSON_B_PERSON_BO_PATIENTB foreign key (ID_PATIENTBOOK)
      references PATIENTBOOK (ID_PATIENTBOOK)
      on delete restrict on update restrict;

