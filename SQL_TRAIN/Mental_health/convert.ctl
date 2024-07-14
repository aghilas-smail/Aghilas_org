LOAD DATA
INFILE 'C:\Users\aghil\Desktop\Aghilas_org\SQL_TRAIN\Mental_health\depression-by-level-of-educatio.csv'
INTO TABLE DEPRESSION_BY_LEVEL_OF_EDUCATION
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
    Entity,
    Code,
    Year,
    All_levels_active,
    All_levels_employed,
    All_levels_total,
    Below_upper_secondary_active,
    Below_upper_secondary_employed,
    Below_upper_secondary_total,
    Tertiary_active,
    Tertiary_employed,
    Tertiary_total,
    Upper_secondary_post_secondary_non_tertiary_active,
    Upper_secondary_post_secondary_non_tertiary_employed,
    Upper_secondary_post_secondary_non_tertiary_total

)