from .constants import (
    STUDENT_ID_COL,
    COURSE_ID_COL,
    ASSIGNMENT_ID_COL,
    TOTAL_SCORE_COL,
    PATTERN_COL_PREFIX,
)


def preprocess_score_df(df):
    df = df.copy()
    df[STUDENT_ID_COL] = df[STUDENT_ID_COL].astype(str)
    df[TOTAL_SCORE_COL] = df[TOTAL_SCORE_COL].astype(float)
    
    pattern_columns = [col for col in df.columns if col.startswith(PATTERN_COL_PREFIX)]
    df[pattern_columns] = df[pattern_columns].astype(float)

    return df


def preprocess_pattern_map_df(df):
    df = df.copy()
    df[COURSE_ID_COL] = df[COURSE_ID_COL].astype(int).astype(str)
    df[ASSIGNMENT_ID_COL] = df[ASSIGNMENT_ID_COL].astype(int).astype(str)

    return df
