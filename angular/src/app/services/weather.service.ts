import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ToastrService} from 'ngx-toastr';
import {BehaviorSubject} from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class WeatherService {

  baseUrl = 'http://127.0.0.1:8000';
  // Weather Data
  private weatherData: any = new BehaviorSubject({});
  sharedweatherData = this.weatherData.asObservable();

  public errors: any = [];

  constructor(private http: HttpClient, private toastr: ToastrService) { }

  public getWeather(data) {
        this.http.get(`${this.baseUrl}/api/locations/${data.city}/?days=${data.days}`).subscribe(
      data1 => {
        this.weatherData.next(data1);

      },
      err => {
        this.toastr.error('Error Retrieving Weather Data', 'Error');
        this.errors = err.error;
        console.log(this.errors);
      }
    );
  }
}
