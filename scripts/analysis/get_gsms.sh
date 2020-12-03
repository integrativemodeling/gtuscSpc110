#!/bin/bash
edc_min_sat=$1
dss_min_sat=$2
<< COMMENT
~/imp-new/build/setup_environment.sh python ~/imp-sampcon/pyext/src/select_good_scoring_models.py -rd ./ -rp run. -sl "CrossLinkingMassSpectrometryRestraint_Distance_|XLDSS" "CrossLinkingMassSpectrometryRestraint_Distance_|XLEDC" -pl Total_Score ExcludedVolumeSphere_gtusc ExcludedVolumeSphere_spc110 ExcludedVolumeSphere_spc110_gtusc ConnectivityRestraint_None -alt $edc_min_sat $dss_min_sat -aut 1.0 1.0 -mlt 0.0 0.0 -mut 35.0 25.0

cd filter
awk '{print $8}' model_ids_scores.txt |grep -v Excluded > ev_gtusc.txt
awk '{print $9}' model_ids_scores.txt |grep -v Excluded > ev_spc110.txt
awk '{print $10}' model_ids_scores.txt |grep -v Excluded > ev_inter.txt
awk '{print $11}' model_ids_scores.txt |grep -v Conn > conn.txt

for kw in ev_gtusc ev_spc110 ev_inter conn
do
	python ~/imp-sampcon/pyext/src/plot_score.py $kw'.txt' $kw >> score_thresholds.txt
done

cd ../

COMMENT

evgtusc_thres=`grep "Mean minus half std_dev" filter/score_thresholds.txt | grep ev_gtusc | awk '{print $NF}'`
evspc110_thres=`grep "Mean minus half std_dev" filter/score_thresholds.txt | grep ev_Spc110 | awk '{print $NF}'`
evinter_thres=`grep "Mean minus half std_dev" filter/score_thresholds.txt | grep ev_inter | awk '{print $NF}'`
conn_thres=`grep "Mean minus half std_dev" filter/score_thresholds.txt | grep conn | awk '{print $NF}'`

~/imp-new/build/setup_environment.sh python ~/imp-sampcon/pyext/src/select_good_scoring_models.py -rd ./ -rp run. -sl "CrossLinkingMassSpectrometryRestraint_Distance_|XLDSS" "CrossLinkingMassSpectrometryRestraint_Distance_|XLEDC" ExcludedVolumeSphere_gtusc ExcludedVolumeSphere_spc110 ExcludedVolumeSphere_spc110_gtusc ConnectivityRestraint_None -pl Total_Score -alt $edc_min_sat $dss_min_sat 0.0 0.0 0.0 -99.9 -aut 1.0 1.0 $evgtusc_thres $evspc110_thres $evinter_thres $conn_thres -mlt 0.0 0.0 0.0 0.0 0.0 0.0 -mut 35.0 25.0 0.0 0.0 0.0 0.0 -e 

