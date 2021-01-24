import { Component, OnInit } from '@angular/core';
import {ToastrService} from 'ngx-toastr';
import {WeatherService} from '../../services/weather.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  city: string;
  days: string;
  maximum: string;
  minimum: string;
  average: string;
  median: string;

  constructor(private weatherService: WeatherService, private toastr: ToastrService) { }

  get_weather() {
    if (!this.city || !this.days ) {
      this.toastr.error('Error, please enter all fields correctly', 'Error');
    } else {
      this.weatherService.getWeather({
        city: this.city,
        days: this.days,
      });
      this.weatherService.sharedweatherData.subscribe(data => {
        this.maximum = data.maximum;
        this.minimum = data.minimum;
        this.average = data.average;
        this.median = data.median;
      } );
    }
  }

  ngOnInit(): void {
  }

}
