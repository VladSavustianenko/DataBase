/*==============================================================*/
/* Table: MATCH                                                 */
/*==============================================================*/
create table MATCH 
(
   TEAM_HOME_NAME       VARCHAR2(50)         not null,
   TEAM_AWAY_NAME       VARCHAR2(50)         not null,
   MATCH_HOME_GOALS     NUMBER,
   MATCH_AWAY_GOALS     NUMBER,
   MATCH_RESULTS        CHAR(1),
   SEASON_PERIOD        VARCHAR2(20)         not null,
   constraint PK_MATCH primary key (TEAM_HOME_NAME, TEAM_AWAY_NAME, SEASON_PERIOD)
);

/*==============================================================*/
/* Table: SEASON                                                */
/*==============================================================*/
create table SEASON 
(
   SEASON_PERIOD        VARCHAR2(20)         not null,
   constraint PK_SEASON primary key (SEASON_PERIOD)
);

/*==============================================================*/
/* Table: TEAM                                                  */
/*==============================================================*/
create table TEAM 
(
   TEAM_NAME            VARCHAR2(50)         not null,
   constraint PK_TEAM primary key (TEAM_NAME)
);

alter table MATCH
   add constraint FK_MATCH_M_T_1_TEAM foreign key (TEAM_HOME_NAME)
      references TEAM (TEAM_NAME);

alter table MATCH
   add constraint FK_MATCH_M_T_2_TEAM foreign key (TEAM_AWAY_NAME)
      references TEAM (TEAM_NAME);

alter table MATCH
   add constraint FK_MATCH_RELATIONS_SEASON foreign key (SEASON_PERIOD)
      references SEASON (SEASON_PERIOD);
