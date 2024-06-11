import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { apiUrl } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FeedbackService {

  backEndAddress: string = apiUrl;

  constructor(private http: HttpClient) { }

  postFeedback(feedback: string): Observable<any>{
    const timeoutDuration = 40000;
    const options = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      }),
      timeout: timeoutDuration
    };
    const data = { "review": feedback }
    return this.http.post(this.backEndAddress + "sentiment-api", data, options);
  }
}
