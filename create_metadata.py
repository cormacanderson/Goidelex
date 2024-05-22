#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import frictionless as fl
import pandas as pd

def make_pattern(series):
    vals = "|".join(str(x) for x in series.values)
    return f"{vals}(;(vals))+"

def pattern_multi_foreignkey(path):
    df = pd.read_csv(path)
    return make_pattern(df.iloc[:,0])

basepath = str(Path(__file__).parent)
package = fl.Package('etc/goidelex_package_schema.json')

package.version = "v1.0.1"
# Correct basepath to be the root dir
package.basepath = basepath
for r in package.resources:
    r.basepath = basepath

# Setup multiple foreign keys relations...
flexemes = package.get_resource("flexemes")
props = flexemes.schema.get_field("inherent_properties")
props.constraints["pattern"] = pattern_multi_foreignkey("inherent_properties.csv")
texts = flexemes.schema.get_field("texts")
texts.constraints["pattern"] = pattern_multi_foreignkey("texts.csv")

# Setup multiple foreign keys relations...
lexemes = package.get_resource("lexemes")
fam = lexemes.schema.get_field("derivational_families")
fam.constraints["pattern"] = pattern_multi_foreignkey("derivational_families.csv")

package.infer()
package.to_json("goidelex.package.json")
