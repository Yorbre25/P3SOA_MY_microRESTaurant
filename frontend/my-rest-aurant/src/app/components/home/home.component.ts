import { Component, OnInit } from '@angular/core';
import { MealRecommendationComponent } from "../meal-recommendation/meal-recommendation.component";
import { ReservationComponent } from "../reservation/reservation.component";
import { FeedbackComponent } from "../feedback/feedback.component";
import { MenuComponent } from "../menu/menu.component";
import { NavbarComponent } from "../navbar/navbar.component";
import { PromoteUserAdminComponent } from '../promote-user-admin/promote-user-admin.component';
import { HttpClient } from '@angular/common/http';
import { UserAccessService } from '../../services/user-access.service';

@Component({
    selector: 'app-home',
    standalone: true,
    templateUrl: './home.component.html',
    styleUrl: './home.component.css',
    imports: [MealRecommendationComponent, ReservationComponent, FeedbackComponent, MenuComponent, NavbarComponent, PromoteUserAdminComponent]
})
export class HomeComponent implements OnInit{

    isAdmin = false;
    userName: string = "";

    constructor(private userAccessService: UserAccessService){}

    ngOnInit(): void {
        console.log({val:sessionStorage.getItem('idToken')})
        if(sessionStorage.getItem('idToken') != null){
            this.userAccessService.isAdmin(sessionStorage.getItem('idToken') ?? '').subscribe(result => {
                this.isAdmin = result != null;
                console.log({resulting: result})
            })
        }
        this.userName = sessionStorage.getItem('email') ?? "";
    }

}
