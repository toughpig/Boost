#!/usr/bin/python

# Copyright 2007 Rene Rivera.
# Copyright 2011 Steven Watanabe
# Distributed under the Boost Software License, Version 1.0. 
# (See accompanying file LICENSE_1_0.txt or http://www.boost.org/LICENSE_1_0.txt) 

import BoostBuild

t = BoostBuild.Tester(pass_toolset=0, pass_d0=False)

t.write("file.jam", """
    actions .a.
    {
echo [$(<:B)] 0
echo [$(<:B)] 1
echo [$(<:B)] 2
    }
    
    rule .a.
    {
        DEPENDS $(<) : $(>) ;
    }
    
    NOTFILE subtest ;
    .a. subtest_a : subtest ;
    .a. subtest_b : subtest ;
    FAIL_EXPECTED subtest_b ;
    DEPENDS all : subtest_a subtest_b ;
""")

t.run_build_system("-ffile.jam -n", stdout="""...found 4 targets...
...updating 2 targets...
.a. subtest_a

echo [subtest_a] 0
echo [subtest_a] 1
echo [subtest_a] 2
    
.a. subtest_b

echo [subtest_b] 0
echo [subtest_b] 1
echo [subtest_b] 2
    
...updated 2 targets...
""")

t.expect_nothing_more()

t.cleanup()
