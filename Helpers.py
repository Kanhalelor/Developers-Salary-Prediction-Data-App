# helper functions

# clean categories
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

# clean years of proffesional coding exp
def clean_years_code_pro(answer):
  if answer == 'Less than 1 year':
    return 1
  if answer == 'More than 50 years':
    return 50
  return float(answer)

# clean educational level
def clean_ed_level(answer):
    if 'Bachelor’s degree' in answer:
        return 'Bachelor’s degree'
    if 'Master’s degree' in answer:
        return 'Master’s degree'
    if 'Professional degree' in answer or 'Other doctoral' in answer:
        return 'Post grad'
    return 'Less than a Bachelors'