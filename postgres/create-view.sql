create or replace view pathwaysdos.elastic_search as
select 
	'{"index": {"_index": "service2", "_type": "service", "_id": '||id||'}}' || chr(10) || row_to_json(t) elastic_bulk_service
from (
	select 
		ser.id, 
		ser.uid, 
		ser.name service_name, 
		ser.odscode, 
		ser.isnational, 
		ser.postcode, 
		ser.easting, 
		ser.northing, 
		typ.name type_name, 
		stat.name status_name,
		dt_times.opening_times,
		ser.modifiedtime last_change_timestamp
	from pathwaysdos.services ser	
	inner join pathwaysdos.servicetypes typ on ser.typeid = typ.id 
	inner join pathwaysdos.servicestatuses stat on ser.statusid = stat.id
	left join (
		select 
		dt_day.serviceid,
		json_agg(dt_day.day_object) opening_times
		from (
			select
				sdo.serviceid,
				sdo.dayid,
				json_build_object(
					'day', otd."name",
					'periods', json_agg(
						json_build_object(
							'start_time', sdot.starttime,
							'end_time', sdot.endtime
						)
					)
				) day_object
			from pathwaysdos.servicedayopenings sdo
			inner join pathwaysdos.servicedayopeningtimes sdot on sdot.servicedayopeningid = sdo.id
			inner join pathwaysdos.openingtimedays otd on otd.id = sdo.dayid
			group by sdo.serviceid, sdo.dayid, otd."name"
		) dt_day
	group by dt_day.serviceid
	) dt_times
	on dt_times.serviceid = ser.id
	--where ser.id in (168, 182) -- examples with multiple periods per day
) t;