import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-iyr',
  templateUrl: './iyr.component.html',
  styleUrls: ['./iyr.component.scss']
})
export class IyrComponent implements OnInit {
  panelExpandedEda = false;
  panelExpandedCyr = false;
  hiddenEda = false;
  hiddenCyr = false;
  constructor() { }

  ngOnInit(): void {
  }
}
