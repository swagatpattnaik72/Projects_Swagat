package com.weatherapp.controller;

import com.weatherapp.model.WeatherRecord;
import com.weatherapp.service.WeatherRecordService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/weather")
@CrossOrigin(origins = "*")  // Optional: allows frontend to access the backend
public class WeatherRecordController {

    @Autowired
    private WeatherRecordService service;

    @GetMapping
    public List<WeatherRecord> getAllRecords() {
        return service.getAll();
    }

    @GetMapping("/{id}")
    public WeatherRecord getRecordById(@PathVariable Long id) {
        return service.getById(id).orElse(null);
    }

    @PostMapping
    public WeatherRecord createRecord(@RequestBody WeatherRecord record) {
        return service.create(record);
    }

    @PutMapping("/{id}")
    public WeatherRecord updateRecord(@PathVariable Long id, @RequestBody WeatherRecord record) {
        return service.update(id, record);
    }

    @DeleteMapping("/{id}")
    public void deleteRecord(@PathVariable Long id) {
        service.delete(id);
    }
}
