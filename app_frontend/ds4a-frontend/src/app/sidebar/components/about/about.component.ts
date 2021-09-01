import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {
  panelExpandedHowDashboard = false;
  panelExpandedWhatApp = false;
  panelExpandedDevelopers = false;
  hiddenHowDashboardButton = false;
  hiddenWhatAppButton = false;
  hiddenDevelopersButton = false;
  constructor() { }

  ngOnInit(): void {
  }

}
