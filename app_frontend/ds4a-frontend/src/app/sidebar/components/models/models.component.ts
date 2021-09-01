import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-models',
  templateUrl: './models.component.html',
  styleUrls: ['./models.component.scss']
})
export class ModelsComponent implements OnInit {
  panelExpandedModel1 = false;
  panelExpandedModel2 = false;
  hiddenModel1 = false;
  hiddenModel2 = false;
  constructor() { }

  ngOnInit(): void {
  }

}
